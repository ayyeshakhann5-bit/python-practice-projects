#Python Reading files (.txt,.json,.csv)

#import json

import csv

file_path="/Users/ayesha.khan/Desktop/output.txt"

try:
  with open(file_path,"r") as file:
   #content=file.read()
    content=csv.reader(file)
    for line in content:
      print(line[1])
    #print(content[1]["Name"])
  
except FileNotFoundError:
    print("File not found")
    
except PermissionError:
  print("You don't have enough permission to read this file")    