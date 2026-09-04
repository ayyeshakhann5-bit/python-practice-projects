class Book:
  
  def __init__(self,title,author,number_of_pages):
    self.title = title
    self.author = author
    self.number_of_pages = number_of_pages
    
  def __str__(self):
    return f"Title: {self.title}, Author: {self.author}, Pages: {self.number_of_pages}" 
  
  def __eq__(self, other):
    return self.title==other.title and self.author==other.author and self.number_of_pages==other.number_of_pages
  
  def __gt__(self, other):
    return self.number_of_pages>other.number_of_pages
  
  def __lt__(self, other):
    return self.number_of_pages<other.number_of_pages 
  
  def __add__(self, other):
    return self.number_of_pages+other.number_of_pages
  
  def __contains__(self, keyword):
    return keyword in self.title or keyword in self.author
  
  def __getitem__(self, key):
    if key=='title':
      return self.title
    
    elif key=='author':
      return self.author
    
    elif key=='number_of_pages':
      return self.number_of_pages
    
    else:
      return f"Key {key} not found"
    
book1= Book("The Great Gatsby","F. Scott Fitzgerald",180) 
book2= Book("To Kill a Mockingbird","Harper Lee",281)
book3= Book("1984","George Orwell",328)

print(book2)    
print("in" in book3)  

print(book1==book2)
print(book1>book2)  

print(book1['author'])
print(book2['title'])
print(book3['Audio'])