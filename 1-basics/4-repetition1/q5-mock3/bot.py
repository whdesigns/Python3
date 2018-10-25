health = 100
print("Your health is 100%. Escape is in progress...")
for number in range(0, 5, 1):
  print("…Oh dear, who is that?" )
  user = str(input())
  
  if (user == "Smiler's Bot"):
    health = health - 20  
    print("Time to jam out of here!")
    
  elif (user == "Hacker"):
    health = health + 20 
    print("Yay! Better follow this one!")
    
  else:
    print("Phew, just another emoji!")
  
  
  print("Escaped Health is", str(health) + "%")

