#python writing files(.txt,.jsn,.csv)


txt_data='I like Pizza'

#file_path='output.txt'
file_path='/Users/ayesha.khan/Desktop/output.txt'

with open(file_path, "w") as file:
     file.write(txt_data)
     print(f"txt file {file_path} is created")
  

