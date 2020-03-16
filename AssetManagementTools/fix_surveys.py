"""
Temporary solution to fix field names and values from survey123 AGO.
"""

import arcpy
import os
# import json

sde_conn = r"C:\Users\avenneman\Documents\Programming\AssetManagementTools\Data\wet_wells.gdb"
sde_table = os.path.join(sde_conn, "LS_wet_well_survey_results")
network_drive = r"C:\Users\avenneman\Documents\Programming\AssetManagementTools\Data\wet_wells.gdb"
survey_result_table = os.path.join(network_drive, "wetwellExcel")


def field_dictionary(esri_table):
    """
    Create two lists: field names and field aliases for the sde
    :param esri_table:
    :return:
    """

    field_list = arcpy.ListFields(esri_table)
    names = []
    aliases = []
    types = []

    for field in field_list:
        print(field.name)
        if field.name == 'x':
            arcpy.DeleteField_management(esri_table, field.name)
        elif field.name == 'y':
            arcpy.DeleteField_management(esri_table, field.name)
        elif field.name == 'OBJECTID_1':
            arcpy.DeleteField_management(esri_table, field.name)
        else:
            aliases.append(field.aliasName)
            names.append(field.name)
            types.append(field.type)
    # iterables = []
    dictionary = sorted(zip(aliases, names, types))

    return dictionary


def alias_compare(sde_alias_table, export_alias_table):
    """
    :param export_alias_table:
    :param sde_alias_table:
    :return:
    """
    sde_field_list = arcpy.ListFields(sde_alias_table)
    sde_alias = []
    export_field_list = arcpy.ListFields(export_alias_table)
    export_alias = []

    for field in sde_field_list:
        sde_alias.append(field.aliasName)
    for e_field in export_field_list:
        export_alias.append(e_field.aliasName)
    # Display number of fields in either table and print differences.
    print("Number of SDE fields: {}\nNumber of Export Fields: {}\n".format(len(sde_alias), len(export_alias)))
    sde_set = set(sde_alias)
    export_set = set(export_alias)
    difference = export_set.difference(sde_set)
    print("Fields in the Export Table not in the SDE Table: {}\n".format(difference))
    reverse_difference = sde_set.difference(export_set)
    print("Now the inverse, fields in the SDE Table not in the Export Table: {}\n".format(reverse_difference))
    # Delete unnecessary fields
    for d in export_field_list:
        if d.name in difference:
            arcpy.DeleteField_management(survey_result_table, d.name)
        else:
            print(d.name)
    # Create dictionary from the two lists of aliases.
    dictionary = dict(zip(sde_alias, export_alias))

    return dictionary


# alias_dictionary = alias_compare(sde_table, survey_result_table)
#
# for k, v in alias_dictionary.items():
#     if k == v:
#         print("Alias in SDE table: {}\nAlias in Exported Table: {}\n*****************".format(k, v))
#     else:
#         print("{} and {} don't match".format(k, v))

# Create dictionaries with aliases, names, and data types.
export_dict = field_dictionary(survey_result_table)
sde_dict = field_dictionary(sde_table)
for e in sde_dict:
    e_alias = e[0]
    e_name = e[1]
    e_type = e[2]
    if e_alias == 'GlobalID':
        del e_alias
    elif e_alias == 'OBJECTID':
        del e_alias
    else:
        arcpy.AddField_management(survey_result_table,
                                  e_name,
                                  e_type,
                                  field_alias=e_alias)
        print("Added {}".format(e_name))
        # TODO use concurrent cursors instead of this crap
        new_table = arcpy.ListFields(survey_result_table)
        # a = 0
        for n in new_table:
            # print("{}: {}".format(n.name, n.aliasName))
            if n.aliasName == e_alias:
                print(n.aliasName, e_alias)

                # a += 1
                # print(a)
                expression = '!{}!'.format(e_name)
                arcpy.CalculateField_management(survey_result_table,
                                                e_name,
                                                expression,
                                                'PYTHON3')
                print("{} Calculated".format(e_name))

new_fields = arcpy.ListFields(survey_result_table)
for n in new_fields:
    print(n.name)
for r in export_dict:
    d_name = r[1]
