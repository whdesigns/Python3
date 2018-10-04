import math

# Read radius from user
print("Please enter radius")
radius = float(input())

# Calculate area and circumference
area = math.pi * (radius * radius)
# alternative 
# math.pi * (radius ** 2)
# math.pi * pow(radius, 2) # Best for more advanced code
circumference = 2 * math.pi * radius

# Display result
print("Area is", round(area, 2))
print("Circumference is", round(circumference, 2))

