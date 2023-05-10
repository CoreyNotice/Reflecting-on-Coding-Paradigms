class Podracer:
  def __init__(self,max_speed,condition,price):
    self.max_speed=max_speed
    self.condition=condition
    self.price=price
  def repair(self):
   self.condition="repaired" 

class AnakinsPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price):
  
  def boost(self):
    self.max_speed *= 2
class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
     super.init(max_speed, condition, price):
    def flame_jet(self,other):
      other.condition = "trashed"

    # how does this solution demonstrate the four pillars of OOP?   

    # Encapaulation: bundling infomation together.
    # the boost and flame_jet methods of the AnakinsPod and SebulbasPod classes modify 
    # the encapsulated max_speed and condition attributes in a safe and controlled manner.

# Abstraction-hiding unnecessary info
# External code can create instances of the Podracer, AnakinsPod, and SebulbasPod 
# classes and interact with their public methods, such as repair, boost, and flame_jet, 
# without needing to know the underlying implementation details.

#  inheritance- reusing code where possible.
# demonstrates inheritance by creating the AnakinsPod and SebulbasPod classes as 
# subclasses of the Podracer class.The Podracer class contains the common
#  attributes and methods that are shared by all Podracer instances, such as
#  max_speed, condition, price, and repair. The AnakinsPod and SebulbasPod 
# classes inherit these attributes and methods from the Podracer class, and 
# can also have their own unique attributes and methods.

# Polymorphism-using same interface for different classes.

# This solution demonstrates polymorphism by allowing different instances 
# of the Podracer class and its subclasses to be treated as instances of 
# the same class and interact with the same methods in different ways.


# Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
# NO, python approch is more direct and consis with functional programing concepts.

# How in particular did Object Oriented Programming assist in the solving of this problem?
# Be creating a code that can be easily altered. can reuse function and restore object.
