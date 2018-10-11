max_robots = 10

print("Enter a number of robots:")
num_robots = int(input())

count = 0
if (num_robots < max_robots):
  while (count < num_robots):
    print("#########")
    print("#       #")
    print("# O   O #")
    print("|   V   |")
    print("|  ---  |")
    print("|_______|")
    count = count + 1

  else:
    while(count < num_robots):
      print("#########")
      print("#       #")
      print("# O   O #")
      print("|   V   |")
      print("|  ---  |")
      print("|_______|")
    count = count + 1
