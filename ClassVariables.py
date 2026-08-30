class Student:
  class_year=2025
  num_students=0
  def __init__(self,name,age):
    
    self.name=name
    self.age=age
    Student.num_students+=1

student1=Student("Ayesha",24) #object
student2=Student("Ptrick",25)
student3=Student("Bob",26)
student4=Student("Peter",28)

"""
print(student1.name)
print(student1.age)
print(Student.class_year)
"""
"""
print(Student.num_students)
"""

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)