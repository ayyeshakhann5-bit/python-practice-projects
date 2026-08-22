
"""
word="APPLE"

Guess=input("Guess any letter:")

if Guess in word:
  print("present")

else:
  print("not")

  """

"""
students={"Aisha","khan"}

student=input("Enter name of student:")

if student not in students:
  print(f"{student} was not found")    

else:
  print(f"{student} is a student")  

"""


grades={"Ayesha":1,
        "Khan":2}

student=input("Enter name of student:")

if student in grades:
  print(f"{student}'s grade is {grades[student]}")

else:
  print(f"{student} was not found") 

