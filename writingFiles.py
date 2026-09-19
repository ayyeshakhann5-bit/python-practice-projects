#python writing files(.txt,.jsn,.csv)

import json

import csv

"""
employee={
  "name":"Ayesha",
  "age":24,
  "Company":"Servicenow"
  
}

"""

employees=[["Name","Age","Job"],
           ["Ayesha",24,"Technical Engineer"],
           ["Khan",25,"SDE"]]



#employees=["Ayesha","khan","Aisha","khannn"]

#file_path='output.txt'
file_path='/Users/ayesha.khan/Desktop/output.txt'

try:
    with open(file_path, "w") as file:
    #with open(file_path, "x") as file:
    #with open(file_path, "a") as file:
         #json.dump(employee,file,indent=5)
         writer=csv.writer(file)
         for row in employees:
           writer.writerow(row)
         print(f"CSV file {file_path} is created")
         
except FileExistsError:
  print("That file already exists")         
         
  

