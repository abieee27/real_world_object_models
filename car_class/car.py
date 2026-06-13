class Car:
    def __init__(self, year_model, car_make):
        self.__year_model = year_model
        self.__car_make = car_make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed