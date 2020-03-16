from Trip import Trip
from MaxMileageException import MaxMileageException

try:
    miles = int(input("How many miles to your destination? \n"))
    trip = Trip()
    trip.setMiles(miles)
    hours = miles / 65
    print ("The trip will be {} hours.".format(hours))
    trip.stop_for_food(hours)
    trip.rest_for_day(hours)
    # print(miles)
    loop = 0
    while miles > 0:
        if loop == 350:
            print("You are getting low on gas. Please fill up.")
        loop += 1
        # print(miles)
        miles -= 1
except MaxMileageException:
    print("You must not go on a trip over 500 miles.")
