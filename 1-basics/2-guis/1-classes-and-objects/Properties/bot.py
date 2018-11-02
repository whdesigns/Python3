class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        if age >= 0:
          self.age = age
        else: 
           self.age = 0

    @property # Gets something, in this case it's getting the age
    def age(self):
        return self._age

    @age.setter # Sets something, in this case it's setting the age to be greater than or equal to 0. Age is then set to value, or failing that a message will appear signifying an error. 
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("Age can't be negative!")

    @property
    def full_name(self):
        return f"{self. first} {self.last}"

    @full_name.setter
    def full_name(self, name):
        self.first, self.last = name.split(" ")

Jane = Human("Jane", "Goodall", 34)
print(Jane.age)
Jane.age = 20
print(Jane.age)
print(Jane.full_name)
Jane.full_name = "Tim Minchin"
print(Jane.full_name)


