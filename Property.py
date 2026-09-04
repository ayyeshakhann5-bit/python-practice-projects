class Rectangle:
    def __init__(self,height,width):
        self._height = height
        self._width = width
        
    @property
    def height(self):
      return f"Height: {self._height}cm"
    
    @property
    def width(self):
      return f"Width: {self._width}cm"    
    
    @height.setter
    def height(self,new_height):
      if new_height<0:
        print("Height cannot be negative")
      else:
        self._height = new_height
        
        
    @width.setter
    def width(self,new_width):
       if new_width<0:
         print("Width cannot be negative")
       else:
         self._width = new_width   
         
         
    @width.deleter
    def width(self):
      del self._width
      print("Width has been deleted")
      
    @height.deleter
    def height(self):
      del self._height
      print("Height has been deleted")
            
        
rectangle=Rectangle(10,20)

rectangle.height=15
rectangle.width=20


"""
print(rectangle.height)
print(rectangle.width)     
"""   

del rectangle.height
del rectangle.width