from pet import Pet

my_pet = Pet()

my_pet.set_pet_name(input("Enter pet name: "))
my_pet.set_animal_type(input("Enter animal type: "))
my_pet.set_pet_age(int(input("Enter pet age: ")))

print("\nPET INFORMATION")
print("Name:", my_pet.get_pet_name())
print("Type:", my_pet.get_animal_type())
print("Age:", my_pet.get_pet_age())