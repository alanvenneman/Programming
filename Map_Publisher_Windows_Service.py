# Publishes a service to machine myserver using Test.mxd
# A connection to ArcGIS Server must be established in the
#  Catalog window of ArcMap before running this script
import arcpy, sys, os, logging, subprocess, shutil, glob, urllib2, urllib, ssl
from time import strftime
import xml.dom.minidom as DOM

logger = logging.getLogger('myapp')
hdlr = logging.FileHandler(strftime('D:\\Temp\\logs\\Test_OverWrite_%H%M%S_%m_%d_%Y.log'))
hdlr.suffix = '%H_%M_%d_%m_%Y.log.log'
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.INFO)
logger.info('--Script Began Running')
logger.info('--End MXD copy from fileshare to local data store.')

# Define local variables
wrkspc = 'D:/MXDs/Test/'
TestMap = arcpy.mapping.MapDocument(wrkspc + 'Test.mxd')
logger.info('-- Local varbles Defined')

# Provide path to connection file
# To create this file, right-click a folder in the Catalog window and
# click New > ArcGIS Server Connection
con = 'D:\Temp\ArcGIS Connection\ArcGISAdminConnection.ags'
logger.info('-- Server Connection Defined')

logger.info('-- Begin overwrite of Test service')
# Provide other service details
TestService = 'Test'
sddraft_Test = wrkspc + TestService + '.sddraft'
sd_Test = wrkspc + TestService + '.sd'

logger.info('-- Create service definition draft of Test service')
# Create service definition draft
arcpy.mapping.CreateMapSDDraft(TestMap, sddraft_Test, TestService, 'ARCGIS_SERVER', con, True, None)
doc = DOM.parse(sddraft_Test)

configProps = doc.getElementsByTagName('Info')[0]
propArray = configProps.firstChild
propSets = propArray.childNodes
for propSet in propSets:
    keyValues = propSet.childNodes
    for keyValue in keyValues:
        if keyValue.tagName == 'Key':
            if keyValue.firstChild.data == "WebCapabilities":
                keyValue.nextSibling.firstChild.data = "Query,Create,Update,Delete"

f = open(sddraft_Test, 'w')
doc.writexml( f )
f.close()

logger.info('-- Analyze the service definition draft')
# Analyze the service definition draft
analysis = arcpy.mapping.AnalyzeForSD(sddraft_Test)


# Print errors, warnings, and messages returned from the analysis
logger.info( 'The following information was returned during analysis of the MXD:')
for key in ('messages', 'warnings', 'errors'):
        logger.info( '----' + key.upper() + '---')
        vars = analysis[key]
        for ((key, code), layerlist) in vars.iteritems():
                logger.info( "'%s' code '%s'", key, code)
                logger.info( '       applies to: ',)
                for layer in layerlist:
                        logger.info( layer.name,)
                #logger.info()

                
# Stage and upload the service if the sddraft analysis did not contain errors
if analysis['errors'] == {}:
        logger.info('-- No errors occured, Service is being published')
        # Execute StageService. This creates the service definition.
        arcpy.StageService_server(sddraft_Test, sd_Test)

       
else:
        logger.info('Service could not be published because errors were found during analysis.')
        print "Service could not be published because errors were found during analysis."
print arcpy.GetMessages()
