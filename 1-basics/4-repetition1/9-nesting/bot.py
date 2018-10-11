print("Please enter a sequence:")
seq = input()

print("Please enter the character of your marker:")
marker = input()

first_marker_position = -1
second_marker_position = -1

for position in range(0, len(seq), 1):
  letter = seq[position]
  if (letter == marker):
    if (first_marker_position == -1):
      first_marker_position = position
    else:
      second_marker_position = position

difference = second_marker_position - first_marker_position - 1
print(difference)
