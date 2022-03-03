import arcpy
import os
import csv


path = r"P:\GIS"
arcpy.env.workspace = path
all_mxds = []


def broken_layer(map_name, layer_object, broken=False):
    """
    This method runs after the layer objects are accessed by the ListLayers method in arcpy.mapping in Python 2.x.
    The purpose of the method is to create a dictionary of layers with the boolean T/F indicating if the layer has a
    broken link or not. The default is false.

    :param map_name:
    :param layer_object:
    :param broken:
    :return:
    """
    import time

    layer_list = []

    if layer_object.supports("dataSource"):
        layer_source = layer_object.workspacePath
    else:
        layer_source = "Null"
    if broken is True:
        localtime = time.asctime(time.localtime(time.time()))
        broken_tuple = (map_name, layer_object.longName, layer_source, "True", localtime)
        layer_list.append(broken_tuple)
        with open('MXD_Report_test3.csv', 'a') as mxd_report_e:
            writer = csv.writer(mxd_report_e)
            for mxd, link, source, broken, time in layer_list:
                writer.writerow([mxd, link, source, broken, time])
        mxd_report_e.close()
        print(broken_tuple)
        return layer_list
    else:
        localtime = time.asctime(time.localtime(time.time()))
        broken_tuple = (map_name, layer_object.longName, layer_source, "False", localtime)
        layer_list.append(broken_tuple)
        with open('MXD_Report_test3.csv', 'a') as mxd_report_e:
            writer = csv.writer(mxd_report_e)
            for mxd, link, source, broken, time in layer_list:
                writer.writerow([mxd, link, source, broken, time])
        mxd_report_e.close()
        print(broken_tuple)
        return layer_list


for root, dirs, files in os.walk(path):
    for f in files:
        if os.path.splitext(f)[1] == '.mxd':
            all_mxds.append(os.path.join(root, f))
total = len(all_mxds)
print("There are {} MXDs in {}".format(total, path))
with open('MXD_Report_test3.csv', 'w') as mxd_report:
    report_writer = csv.writer(mxd_report)
    report_writer.writerow(["Path to MXD", "Layer Name", "Layer Source", "Broken Link?", "Date & Time Scanned"])
try:
    if len(all_mxds) > 0:
        for m in all_mxds:
            mxd_object = arcpy.mapping.MapDocument(m)
            base_name = os.path.basename(mxd_object.filePath)
            mxd_object.title = base_name
            total -= 1
            print("{}: {}".format(total, base_name))

            for l in arcpy.mapping.ListLayers(mxd_object):
                print(l.name)
                if l.isBroken:
                    broken_layer(mxd_object.filePath, l, True)
                else:
                    broken_layer(mxd_object.filePath, l, False)

except RuntimeError as e:
    print("Runtime Error: ", e)
except NameError as n:
    print("Name Error: ", n)
except AttributeError as a:
    print("Attribute Error: ", a)
