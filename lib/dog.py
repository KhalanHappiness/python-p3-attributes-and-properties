#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
   
    def __init__(self, name="Buddy", breed="Pug"):
        # Public attributes that tests will access
        self.name = None
        self.breed = None
        
        # Call setters to validate and set values
        self.set_name(name)
        self.set_breed(breed)
        
    def set_name(self, value):
       
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self.name = value
        else:
            print("Name must be string between 1 and 25 characters.")
    
    def set_breed(self, value):
       
        # Create a case-insensitive comparison
        approved_breeds_lower = [breed.lower() for breed in APPROVED_BREEDS]
        
        if isinstance(value, str) and value.lower() in approved_breeds_lower:
            # Find the correctly capitalized version
            index = approved_breeds_lower.index(value.lower())
            self.breed = APPROVED_BREEDS[index]
        else:
            print("Breed must be in list of approved breeds.")