class DriverAccount:
    def __init__ (self, name, vehicle_plate):
        self.name = name
        self.vehicle_plate = vehicle_plate
        self.__rating = 5.0
        self.__total_trips = 0

    def add_rating(self, new_rating):
        if new_rating < 1.0 or new_rating > 5.0:
            raise ValueError("Invalid Rating!")
        else:
            return new_rating