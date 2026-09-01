class Shape:
  def area(self):
    pass

class Circle(Shape):
  def __init__(self,radius):
    self.radius=radius
    
  def area(self):
    return 3.14*self.radius*self.radius
    

class Square(Shape):
  def __init__(self,side):
    self.side=side

  def area(self):
    return self.side*self.side

class Triangle(Shape):
  def __init__(self,base,height):
    self.base=base
    self.height=height

  def area(self):
    return 0.5*self.base*self.height
  
class Pizza(Circle):
  def __init__(self,radius,toppings):
    super().__init__(radius)
    self.toppings=toppings


shapes=[Circle(4),Square(5),Triangle(6,7),Pizza(15,"cheese")]

for shape in shapes:
  print(shape.area())