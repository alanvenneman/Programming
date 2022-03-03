import arcpy
import os
arcpy.env.workspace = r"\\vs512\e$\avenneman_f\ERP"
arcpy.JSONToFeatures_conversion("CITY_LIMITS_REVERSE.geojson", os.path.join("outgdb.gdb", "CITY_LIMITS_REVERSE"))