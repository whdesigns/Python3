user_word = input("Please enter a word: ")

for char in range(len(user_word) - 1, -1, -1):
  print(user_word[char], end="")
print("\n")
