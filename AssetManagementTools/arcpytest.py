########################
# Title: Survey123 URL Constructor
# Author: Alan Venneman
# Purpose: Gets the itemID and OBJECTID from survey results and joins them to the feature class in Power BI using the
# AssetID. The script will return a URL for a record in survey123.arcgis.com.
# Parameters: Survey result feature class with the following fields:
# 1. ItemID from FGDB name
# 2. OBJECTID
# 3. ASSETID from table of attributes
# 4. Power BI table
# 5. ASSETID from Power BI
########################
import arcpy
import os


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = "toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [PhotoHyperlinks]


class PhotoHyperlinks(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Tool"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        param0 = arcpy.Parameter(
            name="survey_results",
            displayName="Survey Results",
            direction="Input",
            datatype="GPFeature",
            parameterType="Required"
        )

        param1 = arcpy.Parameter(
            name="asset_id",
            displayName="Asset ID Field",
            direction="Input",
            datatype="GPString",
            parameterType="Required"
        )
        param1.parameterDependencies = [param0.name]
        params = [param0, param1]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        if parameters[0].value:
            arcpy.env.workspace = parameters[0].valueAsText
            fcs = arcpy.ListFeatureClasses()
            fcList = []
            for fc in fcs:
                fcList.append(fc)
                parameters[1].filter.list = fcList
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        survey_feature = parameters[0].valueAsText
        asset_field = parameters[1].valueAsText
        return


def main(feature):
    tbx = Toolbox()
    tool = PhotoHyperlinks()
    tool.execute(tool.getParameterInfo(), feature)


path = r"\\vs512\e$\Wastewater Treatment Plant Assessment\1277f367e65d4359bb733eb21c14f098.gdb"
layer = "WWTP_Condition_Assessment_Survey_Version_19"
feature = os.path.join(path, layer)
if __name__ == '__main__':
    main(feature)
