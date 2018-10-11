print("Please enter as a factoral number:")
num = int(input())

fac = 1
for i in range(1, num, 1):
  fac = fac * i
  print("The factorial of ", num, "is ", fac)
  break 
  
