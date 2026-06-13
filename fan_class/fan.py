class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, fan_speed=SLOW, fan_radius=5, fan_color="blue", is_on=False):
        self.__fan_speed = fan_speed
        self.__fan_radius = fan_radius
        self.__fan_color = fan_color
        self.__is_on = is_on

    def get_fan_speed(self):
        return self.__fan_speed

    def set_fan_speed(self, fan_speed):
        self.__fan_speed = fan_speed

    def get_fan_radius(self):
        return self.__fan_radius

    def set_fan_radius(self, fan_radius):
        self.__fan_radius = fan_radius

    def get_fan_color(self):
        return self.__fan_color

    def set_fan_color(self, fan_color):
        self.__fan_color = fan_color

    def get_is_on(self):
        return self.__is_on

    def set_is_on(self, is_on):
        self.__is_on = is_on