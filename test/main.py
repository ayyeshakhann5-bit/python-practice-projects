#Python file detection

import os

file_path="/Users/ayesha.khan/Desktop/test"
if os.path.exists(file_path):
    
    print(f"The file {file_path} exists.")
    
    if os.path.isfile(file_path):
        print("That is a file")
        
    elif os.path.isdir(file_path):
        print("That is a directory")    
    
else:
    print(f"The file {file_path} doesn't exist.")