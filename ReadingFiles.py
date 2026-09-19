#Python Reading files (.txt,.json,.csv)

file_path="/Users/ayesha.khan/Desktop/output"

try:
  with open(file_path,"r") as file:
   content=file.read()
   print(content)
  
except FileNotFoundError:
    print("File not found")