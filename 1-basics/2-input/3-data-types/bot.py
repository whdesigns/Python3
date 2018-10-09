
# Read user data 
print("Please enter your name")
name = input()

print("Please enter your age")
age = int(input() )

print("Please enter your height (m)")
height = float(input()) 

print("Please enter your weight (kg)")
weight = float(input() ) 

bmi  = weight / (height * height)  
print(name, "your bmi is", bmi)
