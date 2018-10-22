print("Please enter a whole number:")
user_number = int(input())
# I created a variable called user_number, which is equal to an integer, meaning it'll only accept whole numbers. I then used parentheses to include the input function, so the user will be able to enter a whole number of their choice. I then placed the question inside another set of parentheses and closed the code with the necessary number of parentheses e.g. 2.  

if user_number% 2==0:
  # I used an if statement to determine if the variable I assigned was even or odd. I did this using a modulo, so I could determine that if the user_number was divided by two and has no remainder, that would make it even. I then used a colon to close the code to ensure it took the argument correctly. 
  print(user_number,"is even")
  # I printed the user_number variable and the words "is even" in string. This message will only appear if the number is even.
else: 
  # An else statement will be used if the number is not even and therefore False. 
  print(user_number,"is odd")   
  # If the number is not even, then the message "is odd" will appear instead of the previous one.  
