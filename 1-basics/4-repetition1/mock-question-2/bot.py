print("Please enter a whole number:")
# The above code uses the string datatype to ask the the user to enter any whole number of their choice.
user_number = int(input())
# I assigned a variable that is equal to the integer datatype, meaning it'll only accept whole numbers. I then used parentheses to include the input function, so the user will be able to enter a whole number of their choice. To ensure its functionality I closed the paretheseses. 
print("Counting Down....")
# As per the specification I used string to compose the message "Counting Down...." before I started work on the numbers. 
for number in range(user_number, 0, -1):
# I decided to use a for loop for this, so I stated that for the number in the range of whatever number the user chose to enter it should decrease by 1, while counting down from whatever that chosen number is. I used a colon to close this function to ensure its functionality. 
   print(number)
# Lastly, I used print and parentheses to call the number that I used for the range in the for loop. This ensures that the code will run and countdown effectively, based on what the user enters.
