# survey_record_url
# constructs a url from the item id in the downloaded survey
#
# example url: https://survey123.arcgis.com/surveys/444872290c8c44ff8a864678eb68338b/data?report=format:docx

import os
import arcpy
import glob
import csv
from xlsxwriter.workbook import Workbook


# Parameters for ArcToolbox tool
folder_path = arcpy.GetParameterAsText(0)  # r'\\svrch02\shared\Public\Asset Management\Lift
# Stations\Photos\LiftStationMay2020\Grounds'
in_geodatabase = arcpy.GetParameterAsText(1)  # os.path.join(
# r'\\svrch02\shared\Public\Asset\Management\Lift\Stations\Photos\LiftStationMay2020\...')
# File I/O - setting environment to Public Drive
folder = os.path.basename(folder_path)
directory = os.path.dirname(folder_path)
os.chdir(directory)
# Isolate itemID string
gdb_split = in_geodatabase.split('_')
itemID = gdb_split[1]
url_string = r"https://survey123.arcgis.com/surveys/{}/data?report=format:docx".format(itemID)
# populate list to add to CSV
my_list = [folder, itemID, url_string]
csv_file = 'TEST_hyperlinks_to_photos.csv'
try:
    # 1. check for csv
    # 2. Either create it, or append to it.
    # 3. Convert to to XLSX
    if not os.path.exists(csv_file):
        with open(csv_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(my_list)
    else:
        with open(csv_file, 'a', newline='') as csvadd:
            writer = csv.writer(csvadd)
            writer.writerow(my_list)

except IOError:
    print("I/O Error")

for csv_file in glob.glob(os.path.join('.', '*.csv')):
    workbook = Workbook(csv_file[:-4] + '.xlsx')
    worksheet = workbook.add_worksheet()
    with open(csv_file, 'rt', encoding='utf8') as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                worksheet.write(r, c, col)
    workbook.close()

# print("Welcome to the Batch Photo hyperlink creator. Please choose your asset group.")
# asset_choice = ["Elevated Storage Tanks", "Facilities", "Ground Water Plants", "Groundwater Storage Tanks",
#                 "Lift Stations", "Parks", "Pavement", "Wastewater Treatment Plants"]
# lift_station_choice = ["Auxiliary", "Grounds", "Odor Control", "Piping", "Pump Controls", "Pump", "SCADA", "Valves",
#                        "Wet Well"]
# increment = 0
# for a in asset_choice:
#     increment += 1
#     print("{}. {}".format(increment, a))
# choices = input('choice: ')
# selected = [int(x) for x in choices.split()]
# if choices == '5':
#     print("Please choose the Lift Station asset survey.")
#     for l in lift_station_choice:
#         increment += 1
#         print("{}. {}".format(increment, l))
#     ls_choices = input('choice: ')
#     ls_selected = [int(x) for x in ls_choices.split()]
