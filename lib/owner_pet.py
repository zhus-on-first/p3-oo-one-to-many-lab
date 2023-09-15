from logging import PercentStyle


class Pet:
    
    all =[]

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    
    def __init__(self, name, pet_type, owner=None) -> None:

        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"""{pet_type} is invalid pet type. 
                            Valid types are: {Pet.PET_TYPES}""")
        
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)


class Owner:

    def __init__(self, name) -> None:
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("Pet must be born of Pet class.")
        pet.owner = self

    def get_sorted_pets(self):
        # get list of owner's pet's
        pets = self.pets()

        # sort with lambda as key
        sorted_pets = sorted(pets, key=lambda pet: pet.name)

        # return sort
        return sorted_pets