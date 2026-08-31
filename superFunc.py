class Shape:
  def __init__(self,color,isFilled):
    self.color=color
    self.isFilled=isFilled
    
  def describe(self):
      print(f"it is {self.color} and {"filled" if self.isFilled else "not filled"}")
    

class Circle(Shape):
  def __init__(self, color, isFilled,radius):
    super().__init__(color, isFilled)
    self.radius=radius
    
  def describe(self):
    super().describe()
    print(f"it is a circle of {3.14*self.radius*self.radius} cm^2")  

class Square(Shape):
  def __init__(self, color, isFilled,width):
    super().__init__(color, isFilled)
    self.width=width
    
  def describe(self):
    super().describe()
    print(f"it is a square of {self.width * self.width} cm^2")      

class Triangle(Shape):
  def __init__(self, color, isFilled,width,height):
    super().__init__(color, isFilled)
    self.width=width
    self.height=height
    
  def describe(self):
    super().describe()
    print(f"it is a triangle of {self.height*self.width/2} cm^2")      
    
circle=Circle("red",True,6)   
sqaure=Square("blue","False",8)
triangle=Triangle("Green","True",2,3)

print(circle.color)
print(circle.isFilled)
print(circle.radius)
circle.describe()

print("*****************")

print(sqaure.color)
print(sqaure.isFilled)
print(sqaure.width)
sqaure.describe()

print("*****************")

print(triangle.color)
print(triangle.isFilled)
print(triangle.width)
print(triangle.height)
triangle.describe()


 
    

