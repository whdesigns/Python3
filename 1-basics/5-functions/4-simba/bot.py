maximum_roars = 3
print("Simba says:")
def roar(num_roars):
  for count in range (0, num_roars,1):
    print("roar!")
  if (num_roars < 3):
    print("cough cough")
  else:
     print("ROARRRRR!!!")
    
  roar(1)
  roar(3)





