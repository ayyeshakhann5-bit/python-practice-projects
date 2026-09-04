class Student:
  
  count=0
  total_gpa=0
  
  def __init__(self,name,gpa):
    self.name = name
    self.gpa = gpa
    Student.count+=1
    Student.total_gpa+=gpa
    
    #instanceMethod
  def get_info(self):
      return f"{self.name}: {self.gpa}"
    
    #classMethod
  @classmethod
  def get_count(cls):
      return f"Total number of students: {cls.count}"
    
  @classmethod
  def gpa_count(cls):
    if(cls.count==0):
      return "No students"
    else:
      return f"Average GPA: {cls.total_gpa/cls.count:.2f}"  
 
student1=Student("John",3.2)
student2=Student("Jane",2.0)
student3=Student("Mike",4.0)
    
print(Student.get_count())    
print(Student.gpa_count())
    
    
    
    