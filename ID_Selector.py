import arcpy
# import xlrd
# import pandas as pd

# Script arguments
subdivision_res = arcpy.GetParameterAsText(0)

dGravity_Main = arcpy.GetParameterAsText(1)
if dGravity_Main == '#' or not dGravity_Main:
   dGravity_Main = "Database Connections\\AlanV.sde\\arcsde.SDE.Utilities_DRAINAGE\\arcsde.SDE.dGravityMain" # provide a default value if unspecified

sGravity_Main = arcpy.GetParameterAsText(2)
if sGravity_Main == '#' or not sGravity_Main:
   sGravity_Main = "Database Connections\\AlanV.sde\\arcsde.SDE.Utilities_SANITARY\\arcsde.SDE.sGravityMain" # provide a default value if unspecified

wPressurized_Main = arcpy.GetParameterAsText(3)
if wPressurized_Main == '#' or not wPressurized_Main:
   wPressurized_Main = "Database Connections\\AlanV.sde\\arcsde.SDE.Utilities_WATER\\arcsde.SDE.wPressurizedMain" # provide a default value if unspecified

# Using Pandas
# excel = pd.read_excel("C:\\Users\\avenneman\\Desktop\\SUBDIVISIONCODE_Test.xlsx", sheetname="Script")

# Reading Excel file using xlrd module.
# wb = xlrd.open_workbook("C:\\Users\\avenneman\\Desktop\\SUBDIVISIONCODE_Test.xlsx")
# sh = wb.sheet_by_name(u'Script')

# Path to ArcMap table view with same data as Excel file above
singlequotes = ("E:\\AVenneman\\LJA Wastewater\\ID_Select_Data.gdb\\WithQuotes")

# Test string with single quotes
name = "Name"
# Test string using .format
test = "{0} = '{1}'".format("NAME_SEC", "ALCORN SECTION TWO")

# Read table view
cursor = arcpy.da.SearchCursor(singlequotes, "Name")
for row in cursor:
    print(row)

    # Alternative Where Clause
    # field = arcpy.AddFieldDelimiters(singlequotes, "NAME_SEC")
    where_clause = "{field} = '{row}'".format(field="NAME_SEC", row=row)

	# Process: Select Subdivision
	subdivision_select = arcpy.SelectLayerByAttribute_management(subdivision_res, "NEW_SELECTION", where_clause)

	# Process: Select dGravity Main
	dgrav_select = arcpy.SelectLayerByLocation_management(dGravity_Main, "INTERSECT", subdivision_select, "", "NEW_SELECTION", "NOT_INVERT")

	# Process: Select sGravity Main
	sgrav_select = arcpy.SelectLayerByLocation_management(sGravity_Main, "INTERSECT", dgrav_select, "", "ADD_TO_SELECTION", "NOT_INVERT")

	# Process: Select wPressurized Main
	wpres_select = arcpy.SelectLayerByLocation_management(wPressurized_Main, "INTERSECT", sgrav_select, "", "ADD_TO_SELECTION", "NOT_INVERT")
