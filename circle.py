import math

def calculate_Area(radius):
    return math.pi * (radius * radius)
    

user_input = float(input("key in your radius:\n"))
print("The area of the radii is:", calculate_Area(user_input))
