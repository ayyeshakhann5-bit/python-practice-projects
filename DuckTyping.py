class Animal:
  alive=False
  
class Dog(Animal):  
  def speak(self):
    print("Woof Woof")
    
class Cat(Animal):
  def speak(self):
    print("Meow Meow")
    
class Car:
  
  alive=False
  def speak(self):
    print("Beep Beep")    
    

animals=[Dog(),Cat(),Car()]
for animal in animals:
  animal.speak()
  print(animal.alive)
  
  
  