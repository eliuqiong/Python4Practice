class Car:
    """inital car info"""

    def __init__(self, make, model, year):
        """initialize the default value"""
        self.make  = make
        self.model = model
        self.year = year

    def get_car_info(self):
        long_name = f"This is a {self.make} {self.year} {self.model}."
        return long_name