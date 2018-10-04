print("Where should I look?")
print("In the bedroom")
print("In the bathroom")
print("In the lab")

place = (input())

if (place == "in the bedroom"):
  print("Where in the bedroom?")
  print("Under the bed")
  print("somewhere else")

  bedroom_place = input()

  if(bedroom_place == "under the bed"):
    print("Found some socks but no battery!")
    else:
    print("Found some mess but no battery!")

