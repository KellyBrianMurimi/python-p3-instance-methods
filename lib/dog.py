#!/usr/bin/env python3

class Dog:
    def __init__(self, name="Fido"):
        self.name = name

    def bark(self):
        print("Woof!")

    def sit(self):
        print(f"The dog is sitting.")

fido = Dog("Fido")
fido.bark()
fido.bark()
fido.sit()
