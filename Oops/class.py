class Dog:

    def __init__(self, name, breed):
        self.name = name  # Instance attribute
        self.breed = breed  # Instance attribute

    def bark(self):
        return f"{self.name} says Woof!"

dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "German Shepherd")

print(dog1.name) 
print(dog2.breed) 
print(dog1.bark())  