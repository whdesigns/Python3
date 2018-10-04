# Useful constants
DAYS_IN_YEAR = 365.25

print("Please enter your age (years)")
age_in_years = int(input())

# Calculate age in days
age_in_days = age_in_years * DAYS_IN_YEAR

# Display result
print("Your age in days is", round(age_in_days, 2))

