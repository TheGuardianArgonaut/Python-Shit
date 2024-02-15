#!/usr/bin/python3
class Dog:
    """Doggy Class"""
    def __init__(self, name, age):
        """Initialize dog with name and age"""
        self.name = name
        self.age = age

gary = Dog("Gary", 4)
print(f"{gary.age }")