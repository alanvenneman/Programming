import csv
import os.path

"""
vlookup is a text-based version of Excel's VLOOKUP function. The workspace, inputs, and outputs of this tool are all
hard-coded and should be changed for this to be a useful tool. After the files are opened, an empty dictionary is created
and filled with the entirety of index.csv using a for loop. The next for loop uses an if statement to check if each item
in the dictionary also exists in data_array.csv. If it does, the item gets appended to the VlookupOut file.

"""
workspace = r"C:\Users\avenneman\Documents\Programming"

with open(os.path.join(workspace, 'data_array.csv'), 'r') as lookuplist:
    with open(os.path.join(workspace, 'index.csv'), 'r') as csvinput:
        with open(os.path.join(workspace, 'VlookupOut'), 'w') as output:

            array = csv.reader(lookuplist)
            index = csv.reader(csvinput)
            writer = csv.writer(output)

            d = {}
            for xl in index:
                d[xl[0]] = xl[1:]

            for i in array:
                if i[0] in d:
                    i.append(d[i[0]])
                writer.writerow(i)
