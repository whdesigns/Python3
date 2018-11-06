class A:
  def __init__(self, name, occupation):
    self.name = name 
    self.occupation = occupation
    print("Assignment due soon :(")
    
class B(A):
  def __init__(self, name, occupation):
    super().__init__(name, occupation)


class C(A):
  def __init__(self, name, occupation):
    super().__init__(name, occupation)


c = C("Name: Will", "Occupation: Student")
c = C("Name: Will Hughes", "Occupation: Web Designer")
print(c.name)
print(c.occupation)
