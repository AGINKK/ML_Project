from abc import ABC, abstractmethod


# 1. ABSTRACTION: Define a blueprint that cannot be instantiated directly
class Person(ABC):

    @abstractmethod
    def get_role(self):
        pass


# 2. INHERITANCE & ENCAPSULATION
class Student(Person):

    def __init__(self, name, age, course):
        self.name = name  # Public attribute
        self._course = course  # Protected attribute (convention)
        self.__age = age  # Private attribute (Encapsulation)

    # Getter method to safely access private age
    def get_age(self):
        return self.__age

    # Setter method to safely modify private age with validation
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Please enter a valid age!")

    # Implementing the abstract method
    def get_role(self):
        return "General Student"


# 3. INHERITANCE & POLYMORPHISM: Creating a specialized subclass
class InternationalStudent(Student):

    def __init__(self, name, age, course, country):
        super().__init__(name, age, course)
        self.country = country

    # Overriding the method (Polymorphism)
    def get_role(self):
        return "International Student"


# --- Testing the Code ---

# Creating an object of the subclass
student1 = InternationalStudent("Agin", 21, "MCA", "India")

# Accessing attributes and methods
print(f"Name: {student1.name}")
print(f"Age: {student1.get_age()}")  # Accessed safely via getter
print(f"Course: {student1._course}")
print(f"Country: {student1.country}")
print(f"Role: {student1.get_role()}")