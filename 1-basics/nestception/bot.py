print("Where should I look?")
print("In the bedroom")
print("In the bathroom")
print("In the lab")

place = (input())

if (place == "in the bedroom"):
  print("Where in the bedroom?")
  print("Under the bed")
  print("Somewhere else")

  bedroom_place = input()

  if(bedroom_place == "in the bathtub"):
    print("Found some socks but no battery!")
    else:
    print("Found some mess but no battery!")


   second_place = (input())

    if (second_place == "In the bathroom"):
  print("Where in the bathroom?")
  print("In the bathtub")
  print("Somewhere else")

  bathroom_place = input()

  if(bathroom_place == "In the bathtub!"):
    print("Found a rubber duck but no battery!")
    else:
    print("It's wet and there is no battery!")


third_place = (input())

    if (third_place == "in the lab"):
  print("Where in the lab?")
  print("On the table, found the battery")
  print("Somewhere else")

  lab_place = input()

  if(lab_place == "In the lab!"):
    print("Found battery in the lab!")
    else:
    print("I don't know where the battery is but I will keep looking")




