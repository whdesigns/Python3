import math

print("Would you like to calculate a cylinder or a cone?")
shape = input()


print("Please enter the radius of the shape")
radius = float(input())

print("Please enter the height of the shape")
height = float(input())

if (shape == "cylinder"):
  volume = (math.py * (radius ** 2 *) * height) / 3
  print("The volume of the cylinder is", volume)
else: 
  print("I dont't know")
  



