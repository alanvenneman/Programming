import arcpy


arcpy.env.workspace = r"C:\Users\avenneman\AppData\Roaming\ESRI\Desktop10.6\ArcCatalog\NewDefault.sde"
arcpy.AssignDomainToField_management(in_table="GISSDE.SDE.LS_control_survey_results",
                                     field_name="panel_box_hinges",
                                     domain_name="cvd_panel_box_hinges",
                                     subtype_code="")
