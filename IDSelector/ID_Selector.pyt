import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [IDSelector]


class IDSelector(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "IDSelector"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        param0 = arcpy.Parameter(
            name="subdiv",
            displayName="Polygon Feature",
            direction="Input",
            datatype="GPFeatureLayer",
            parameterType="Required"
        )

        param1 = arcpy.Parameter(
            name="namesec",
            displayName="Where Clause Field",
            direction="Input",
            datatype="Field",
            parameterType="Required"
        )
        param1.parameterDependencies = [param0.name]

        param2 = arcpy.Parameter(
            name="sgrav",
            displayName="Line Feature 1",
            direction="Input",
            datatype="GPFeatureLayer",
            parameterType="Required"
        )

        param3 = arcpy.Parameter(
            name="dgrav",
            displayName="Line Feature 2",
            direction="Input",
            datatype="GPFeatureLayer",
            parameterType="Optional"
        )

        param4 = arcpy.Parameter(
            name="wpress",
            displayName="Line Feature 3",
            direction="Input",
            datatype="GPFeatureLayer",
            parameterType="Optional"
        )
        params = [param0, param1, param2, param3, param4]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        subdiv = parameters[0].valueAsText
        namesec = parameters[1].valueAsText
        sgrav = parameters[2].valueAsText
        dgrav = parameters[3].valueAsText
        wpress = parameters[4].valueAsText

        # # where_list = []
        # cursor = arcpy.da.SearchCursor(subdiv, namesec)
        # for row in cursor:
        #     where = 'NAME_SEC = ' + "'%s'" %row
        #     print(where)

        # return

    def sqlUpdate(self, polygon, line):
        """Instead of using Search and Update cursors, use SQL directly to add the Project codes to the lines faster."""
        import sqlite3


        """
        The SQL code will be tested then written out here. We need to programattically set the polygon (subdivision) layer
        to a table view and the line to another table view. From there a few queries should be sufficient to move the 
        Project code field to the polyline table.
        
        :param polyline
        :param line
        """