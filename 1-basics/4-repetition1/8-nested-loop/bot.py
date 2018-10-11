print("How many rows would you like?")
num_rows = int(input())

print("How many columns would you like?")
num_cols = int(input())

print("Here I go")

for row in range(0, num_rows, 1):
    for column in range(0, num_cols, 1):
      print(":-)", end="")
    print()

print("Done!")
   


