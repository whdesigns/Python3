def displayLargest(num1, num2):
# This was the default function the brief required me to use. The function has two parameters, which are num1 and num2. 
  if (num1 > num2):
 # I used an "if statement" with a "greater than" comparison operator to determine if num1 is more than num2.
    print("The first number is larger")
  # This message will be displayed on screen if the first number is the larger of the two. 
  elif (num2 > num1):
  # I used an "elif statement" with another "greater than" comparison operator to determine if num2 is larger than num1. This will only be called if the "if statement" was False.
    print("The second number is larger")
    # This message will be displayed on screen if the second number is the larger of the two. 
  else: 
    # If both the if and elif statements are False then the else statement will be called. 
    print("Both numbers are equal")
    # This message will only appear on screen if both the if and elif statements are False, making the else statement the only other outcome that could be True. 


displayLargest(7, 5)
displayLargest(1, 3)
displayLargest(4, 4)
