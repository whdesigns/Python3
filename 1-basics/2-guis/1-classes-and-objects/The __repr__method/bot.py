class User:
  
  active_users = 0

  @classmethod
  def display_active_users(cls): # when a classmethod is called the Class User is passed in. Name the parameter something that makes sense e.g. cls. 
    return f"There are currently {cls.active_users} active users"

  @classmethod 
  def from_string(cls, data_str):
      first,last,age = data_str.split(",")
      return cls(first, last, int(age))
      # cls refers to class
      # This class method will create a brand new user
  
  def __init__(self, first, last, age):
    self.first = first
    self.last = last 
    self.age = age 
    User.active_users += 1


     # turns string into a readable format
  def __repr__(self):
    return f"{self.first} is {self.age}"
  
  def logout(self):
    User.active_users -= 1
    return f"{self.first} has logged out"

  def full_name(self):
    return f"{self.first} {self.last}"

  def initials(self):
    return f"{self.first[0]}.{self.last[0]}"

  def likes(self, thing):
    return f"{self.first} likes {thing}"

  def is_senior(self):
    return self.age >= 65

  def birthday(self):
    self.age += 1
    return f"Happy {self.age}th, Birthday {self.first}"
  
#user1 = User("Will", "Hughes", 28)
#user2 = User("Helena", "Freestone", 40)
#print(User.display_active_users())
#user1 = User("Will", "Hughes", 28)
#user2 = User("Helena", "Freestone", 40)
#print(User.display_active_users())
#tom = User.from_string("Tom,Jones,89")

# Below is used to call the __repr__ function
j = User("Judy", "Steele", 18)
j = str(j)
print(j)
