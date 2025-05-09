#!/usr/bin/env python3

class Person:
    # Class body goes here
    name = "Person"
    #Instance method definition
    def talk(self):
        print("Hello World!")
    
    def walk(self):
        print(f"The {self.name.lower()} is walking.")