class Pet:
    def __init__(self):
        self.__pet_name = ""
        self.__animal_type = ""
        self.__pet_age = 0

    def set_pet_name(self, pet_name):
        self.__pet_name = pet_name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_pet_age(self, pet_age):
        self.__pet_age = pet_age

    def get_pet_name(self):
        return self.__pet_name

    def get_animal_type(self):
        return self.__animal_type

    def get_pet_age(self):
        return self.__pet_age