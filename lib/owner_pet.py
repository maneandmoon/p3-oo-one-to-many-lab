class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

#      validate that the `pet_type` is one of those types in the `__init__` method.
#   - `raise Exception` if this check fails.

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f'pet_type must be one of {Pet.PET_TYPES}')
        
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        Pet.all.append(self)

# - `Owner` and `Pet` should use `isinstance` to check types whenever instances
#   are passed into methods.
#   - `raise Exception` if these checks fail.

class Owner:
    def __init__(self, name):
        self.name = name
    
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("pet must be an instance of Pet")
        pet.owner = self

    def get_sorted_pets(self):
        def get_pet_name(pet):
            return pet.name
        return sorted(self.pets(), key=get_pet_name)

    