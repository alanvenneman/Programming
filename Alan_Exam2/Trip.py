from MaxMileageException import MaxMileageException

class Trip:
    def __init__(self):
        self.hours = 0
        self.miles = 0

    def setMiles(self, miles):
        if miles > 500:
            raise MaxMileageException (miles)
        else:
            self.miles = miles

    def getMiles(self):
        return self.miles

    def stop_for_food(self, hours):
        if hours > 3:
            print("Your passengers are hungry. Please stop for a 45 minute break.")

    # def stop_for_gas(self, miles):
    #     if miles == 350:
    #         print("You are getting low on gas. Please stop to fill up.")

    def rest_for_day(self, hours):
        if hours > 7:
            print("You have driven enough. Please stop for the day.")
