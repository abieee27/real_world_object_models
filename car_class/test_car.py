from car import Car

my_car = Car(2024, "Toyota")

print("Accelerating...")
for i in range(5):
    my_car.accelerate()
    print("Speed:", my_car.get_speed())

print("\nBraking...")
for i in range(5):
    my_car.brake()
    print("Speed:", my_car.get_speed())