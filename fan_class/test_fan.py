from fan import Fan

fan_1 = Fan(Fan.FAST, 10, "yellow", True)
fan_2 = Fan(Fan.MEDIUM, 5, "blue", False)

print("FAN 1")
print("Speed:", fan_1.get_fan_speed())
print("Radius:", fan_1.get_fan_radius())
print("Color:", fan_1.get_fan_color())
print("Is On:", fan_1.get_is_on())

print("\nFAN 2")
print("Speed:", fan_2.get_fan_speed())
print("Radius:", fan_2.get_fan_radius())
print("Color:", fan_2.get_fan_color())
print("Is On:", fan_2.get_is_on())