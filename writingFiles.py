#python writing files(.txt,.jsn,.csv)


employees=["Ayesha","khan","Aisha","khannn"]

#file_path='output.txt'
file_path='/Users/ayesha.khan/Desktop/output.txt'

try:
    with open(file_path, "w") as file:
    #with open(file_path, "x") as file:
    #with open(file_path, "a") as file:
         for employee in employees:
           file.write(employee+" ")
         print(f"txt file {file_path} is created")
         
except FileExistsError:
  print("That file already exists")         
         
  

