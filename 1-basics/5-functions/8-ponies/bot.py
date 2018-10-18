def sum_ages_of_friends(applejack_age, rainbowdash_age, buttershine_age):
  total = applejack_age + rainbowdash_age + buttershine_age
  return total


def calc_avg_age_of_friends(applejack_age, rainbowdash_age, buttershine_age):
  average_age = (applejack_age + rainbowdash_age + buttershine_age) / 3
  return average_age


  def run():
    
    print("Please enter the age for applejack")
    age_1 = int(input())

    print("Please enter 'sum' or 'average'")
    age_2 = int(input())

    print("Please enter the age for buttershine")
    age_3 = int(input())

    print("Please enter 'sum' or 'average'")
    action = str(input())

    if (action == "sum"):
      print( sum_ages_of_friends(age_1, age_2, age_3) )
    
    else: (action == "average"):
      print( calc_avg_age_of_friends(age_1, age_2, age_3) )

  

