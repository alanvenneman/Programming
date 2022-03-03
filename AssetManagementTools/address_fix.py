# import arcpy

addy = '123 SH 6'


def street_dir(situs):
    directions = ['N', 'E', 'S', 'W', 'NE', 'NW', 'SE', 'SW']
    addy_parts = situs.split(" ")
    if len(addy_parts[1]) == 1:
        print("Number " + addy_parts[1])
        if addy_parts[1] in directions:
            return addy_parts[1]
    elif len(addy_parts[0]) <= 2:
        print("Cardinal " + addy_parts[0])
        if addy_parts[0] in directions:
            print("letters correct")
            return addy_parts[0]
    else:
        return " "


# print(street_dir(addy))


def house_num(situs):
    addy_parts = situs.split(" ")
    if addy_parts[0].isdigit():
        return addy_parts[0]
    if addy_parts[1].isdigit():
        return addy_parts[1]


def delete_house_number(situs):
    addy_parts = situs.split(" ")
    if addy_parts[0].isdigit():
        del addy_parts[0]
        return " ".join(addy_parts)
    else:
        return " ".join(addy_parts)


print(delete_house_number(addy))
