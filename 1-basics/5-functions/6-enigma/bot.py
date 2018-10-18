def run():
  print("Please enter a character to display")
char = input()
print("Your character is, char")
print("Please enter a total number of characters")
total_char = int(input())
print("Yourn total number of characters is, total_char")
print("Please enter a whole number")
whole_num = int(input())
print("Your number is, whole_num")

for count in range(1,total_char+1,1):
  if (count % whole_num == 0):
    print(char, end="")
  else:
    print(" ", end="")
