#Python Reading files (.txt,.json,.csv)

file_path="/Users/ayesha.khan/Desktop/output.txt"

try:
  with open(file_path,"r") as file:
   content=file.read()
   print(content)
  
except FileNotFoundError:
    print("File not found")
    
except PermissionError:
  print("You don't have enough permission to read this file")    