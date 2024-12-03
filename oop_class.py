# Access Class Attributes Using Objects
class Bike:
    name = ""
    gear = 0


bike1 = Bike()
bike2 = Bike()
bike1.name = "Mountain Bike"
bike1.gear = 11
bike2.name = "Black Mamba"
bike2.gear = 7

print(f"Name: {bike1.name}, Gears: {bike1.gear}")
print(f"Name: {bike2.name}, Gears: {bike2.gear}")