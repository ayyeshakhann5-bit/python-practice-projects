
class Animal:
  def __init__(self,name):
    self.name=name
  
  
  
  def eat(self):
    print(f"{self.name} is eating")
    
  def sleep(self):
    print(f"{self.name} is sleeping")  


class prey(Animal):
  def flee(self):
    print(f"{self.name} is fleeing")

class predator(Animal):
  def hunt(self):
   print(f"{self.name} is hunting")

class rabbit(prey):
  pass

class hawk(predator):
  pass

class fish(prey,predator):
  pass

rabbit1=rabbit("Tony")
hawk1=hawk("Pony")
fish1=fish("Gony")

rabbit1.flee()
  