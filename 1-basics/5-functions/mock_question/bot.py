def displaySmallest(num1, num2):
# This was the default function the brief required me to use. The function has two parameters, which are num1 and num2. 
  if (num1 < num2):
 # I used an "if statement" with a "less than" comparison operator to determine if num1 is less than num2.
    print("The first number is smaller")
  # This message will be displayed on screen if the first number is the smallest of the two. 
  elif (num2 < num1):
  # I used an "elif statement" with another "less than" comparison operator to determine if num2 is less than num1. This will only be called if the "if statement" was False.
    print("The second number is smaller")
    # This message will be displayed on screen if the second number is the smallest of the two. 
  else: 
    # If both the if and elif statements are False then the else statement will be called. 
    print("Both numbers are equal")
    # This message will only appear on screen if both the if and elif statements are False, making the else statement the only other outcome that could be True. 


displaySmallest (7, 5)
displaySmallest (1, 3)
displaySmallest (4, 4)
# This is used to call the function in order to determine the results. The code will not run unless the function is called with the code above. 


