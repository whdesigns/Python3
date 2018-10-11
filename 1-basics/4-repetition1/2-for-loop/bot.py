max_robots = 10

print("Enter a number of robots:")
num_robots = int(input())

if(num_robots < max_robots):
  for count in range(0,num_robots,1):
    print("#########")
    print("#       #")
    print("# O   O #")
    print("|   V   |")
    print("|  ---  |")
    print("|_______|")
else:
  for count in range(0, max_robots, 1):
      print("#########")
      print("#       #")
      print("# O   O #")
      print("|   V   |")
      print("|  ---  |")
      print("|_______|")
