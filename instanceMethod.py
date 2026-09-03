class Employee:
  def __init__(self,name,position):
    self.name=name
    self.position=position
    
  def get_info(self):
      return f"{self.name} is a {self.position}"
    
    
  @staticmethod
  def is_valid_position(position):
      valid_position=["Manager","Developer","Designer"]
      return position in valid_position
    
    
employee1=Employee("John","Manager")
employee2=Employee("Alice","Developer")
employee3=Employee("Bob","Designer")
    
print(Employee.is_valid_position("Manager"))    
print(employee1.get_info())

print(Employee.is_valid_position("Intern"))


    
    
      