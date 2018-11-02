class Animal: # This is a parent class
  cool = True # This variable is set to True

  def make_sound(self, sound): #This is a function with a parameter called sound)                           
    print(f"This animal says {sound}")

class Cat(Animal): #IMPORTANT: This is a Child Class, because the parent is inside the parenthesis. 
  pass # Must add if there is nothing further otherwise Python will bring up an error


#a = Animal() # This is setting a = to the "parent" Animal.
#a.make_sound("roar!") # This is used a (parent) to called the function make_sound

blue = Cat()
print(isinstance(blue, Cat)) #This should be True, because, blue is equal to the child class "Cat". Using isinstance compares whether the variable is equal or True to something

# It would also be true if Cat was replaced with "object" or "Animal"
