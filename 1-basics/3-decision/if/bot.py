# Read direction from user
print("Please enter one of the following directions:")
print("[w] to go up")
print("[s] to move down")
print("[a] to move left")
print("[d] to move right")

direction = input()

# Work out which direction move input
if (direction == "w"):
  print("I am moving up!")
else: 
  print("I don't know what direction that is!")
