# This is a class (blue print)
class Bot:

  # initial state of a Bot
  def __init__(self, name, age=0, energy=100, shield=100):
    self.name = name
    self.age = age
    self.energy = energy
    self.shield = shield

  # behaviours of a Bot
  def display_name(self):
    print(self.name)

  def display_age(self):
    print(self.age)

  def display_energy(self):
    print(self.energy)

  def display_shield(self):
    print(self.shield)

  def display_summary(self):
    print("Name is {}. Age is {}. Shield is {}. Energy is {}.".format(self.name, self.age, self.energy, self.shield))
   
