class A:
  def option(self):
    print("first test")

    
class A:
  def option(self):
    print("second test")

class C(A):
  def option2(self):
    print("final test")


c = C()
c.option()
c.option2()
