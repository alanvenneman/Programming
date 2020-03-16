#Date:  March 2019
#Purpose:  Generate AssetIDs

import arcpy, os, re, pyodbc

#Delete temp SDE connection as it will be re-created below
try:
    os.remove(r"C:\temp\TestDB.sde")
except:
    pass

#Reconcile and compress SDE
try:
    sde = arcpy.CreateDatabaseConnection_management(r"C:\temp", "TestDB", "SQL_SERVER", "GIS3", "OPERATING_SYSTEM_AUTH", "", "*****", "SAVE_USERNAME", "water_test", "", "TRANSACTIONAL", "sde.DEFAULT", "")
    arcpy.env.workspace = str(sde)
    print str(sde) + " is no longer accepting connections"
    arcpy.AcceptConnections(sde, False)     #block new connections to the database
    try:
        print "Disconnecting all users"
        arcpy.DisconnectUser(sde, "ALL")        #disconnect all users from the database
    except:
        print ""
        raw_input("Insufficient privileges to disconnect users.  Press ENTER to exit.")
        quit()
    print "Compiling a list of versions to reconcile"
    versionList = arcpy.ListVersions(sde)       #list of versions to pass into the ReconcileVersions tool
    print "Reconciling all versions"
    arcpy.ReconcileVersions_management(sde, "ALL_VERSIONS", "sde.DEFAULT", versionList, "LOCK_ACQUIRED", "NO_ABORT", "BY_OBJECT", "FAVOR_TARGET_VERSION", "POST", "DELETE_VERSION", "")

    print "Running compress"
    con = pyodbc.connect("DRIVER={SQL Server};Server=GIS3;DATABASE=water_test;Trusted_Connection = Yes")
    cur = con.cursor()
    row_count = len(cur.execute("select * from sde.sde_state_lineages").fetchall())
    #print cur.execute("select * from sde.sde_state_lineages").fetchall()
    print "SDE is at State " + str(row_count - 1)
    while row_count <> 1:      #compress the database until State 0 is achieved (i.e. one record exists in the lineage table)
        arcpy.Compress_management(sde)
        row_count = len(cur.execute("select * from sde.sde_state_lineages").fetchall())
        #print cur.execute("select * from sde.sde_state_lineages").fetchall()
        print "SDE is at State " + str(row_count - 1)
    cur.close
    con.close
    print "Compress successfully completed!"

    print "Allow users to connect to " + str(sde)
    arcpy.AcceptConnections(sde, True)      #allow the database to begin accepting connections again
    print "Rebuilding indexes on the system tables"
    arcpy.RebuildIndexes_management(sde, "SYSTEM")      #rebuild indexes on the system tables
    print "Updating statistics on the system tables"
    arcpy.AnalyzeDatasets_management(sde, "SYSTEM")
    print ""
    print "Generating Asset IDs..."
    print ""
except arcpy.ExecuteError:
    print ""
    print(arcpy.GetMessages(2))
    print ""
    raw_input("Compression failure.  Press ENTER to exit.")
    quit()

#Generate Asset IDs
try:
    #Feature Class and infrastructure prefix lists need to be insync ordinally
    fclist = ["water_test.WSDTEST.wHydrant", "water_test.WSDTEST.wSystemValve", "water_test.WSDTEST.wPressurizedMain"]
    prefix = ["WT.FH.A", "WT.SV.A", "WT.PM.A"]

    i = 0
    j = 0

    #Find largest ID integer and add 1 to it for new ID integer
    for featclass in fclist:
        if featclass == fclist[i]:
            asset_id_list = [row[0] for row in arcpy.da.SearchCursor(fclist[i], "ASSETID")]        #add all AssetIDs to a list
            int_list = []
            for asset_id_num in asset_id_list:
                if asset_id_num is None:        #ignore NULL values
                    j = j + 1
                    continue
                if asset_id_num.startswith(prefix[i]):      #only work with valid AssetIDs
                    asset_id_num = re.sub('.*0', '0', asset_id_list[j])[1:]     #remove everything but the integer from the AssetID
                    int_list.append(asset_id_num)       #add each value from above to int_list
                    j = j + 1
                    continue
                else:       #ignore invalid values like blanks, numbers, characters, etc
                    j = j + 1

            int_list = [x for x in int_list if x.isdigit()]     #remove non-numerics from the list
            int_list = map(int, int_list)       #convert unicode characters to integers
            new_int = max(int_list) + 1

        #Populate rows where ASSETID is NULL
        counter = 0
        flag = False
        edit = arcpy.da.Editor(sde)     #workspace for edit session
        edit.startEditing(False, True)      #start edit session without an undo/redo stack for versioned data
        edit.startOperation()       #start an edit operation (required for networks)
        rows = arcpy.UpdateCursor(featclass)
        for row in rows:
            if row.ASSETID is None:    #check if value is NULL
                try:
                    row.setValue('ASSETID', prefix[i] + str(new_int).zfill(9))
                    rows.updateRow(row)
                    del row     #delete row object to remove locks on the data
                    counter = counter + 1
                    print featclass + " Asset ID " + prefix[i] + str(new_int).zfill(9) + " added"
                    flag = True
                    new_int = new_int + 1
                except arcpy.ExecuteError:
                    edit.stopOperation()
                    edit.stopEditing(False)     #stop the edit session and do not save the changes
                    print(arcpy.GetMessages(2))
                    raw_input("Asset ID generation failure.  No Asset IDs generated for " + featclass +  " and possibly other Feature Classes.  Press ENTER to exit.")
                    quit()
            else:       #don't do anything if value is not NULL
                continue

        if flag:
            print str(counter) + " " + featclass + " added"
            print ""
        else:
            print "No " + featclass + " Asset IDs to generate"
            print ""

        edit.stopOperation()        #stop the edit operation
        edit.stopEditing(True)      #stop the edit session and save the changes
        j = 0
        i = i + 1
except Exception as e:
    try:
        if edit.isEditing:
            edit.stopOperation()
            edit.stopEditing(False)
    except:
        pass

    print ""
    print e.message
    print ""
    raw_input("Press ENTER to exit")
    quit()