# Read current amount from user

print("Please enter the current amount")
current_amount = float( input() )
# read interest rate from user
print("Please enter an interst rate (%)")
interest_rate = float( input() )

# Work out new amount
interest_amount = interest_rate / 100) * current_amount
new_amount = current_amount + interest_amount

# Display the result
print("Your new amount is", round(new_amount, 2) )
