#a function is a block of code

"""def dispaly_invoice(username,amount,due_date):
  print(f"Hello {username}")
  print(f"your bill {amount:.2f} is due date for {due_date}")

dispaly_invoice("Ayesha",34.789,"01/08")

print("test")
"""

"""ddef full_name(first,last):
  first_name=first.capitalize()
  last_name=last.capitalize()
  return first_name+" "+last_name
name=full_name("aisha","khan")
print(name)
"""

"""
def net_price(price,discount=0,tax=0.05):
  return price*(1-discount)*(1+tax)

print(net_price(500))
"""

"""
import time

def count(start,end):
    for x in range(start,end+1):
        print(x)
        time.sleep(0.2)
    print('DONE!')

count(0,5)    

"""

"""

def get_phone(country,area,first,last):
  return f"{country}-{area}-{first}-{last}"

phone_num=get_phone(country=+91,area=878,first=701,last=2844)
print(phone_num)

"""
"""
def add(*args):
  total=0
  for arg in args:
    total+=arg
  return total

print(add(1,2,3))  

"""
"""
def display_name(*args):
  for arg in args:
    print(arg, end=" ")

display_name("ayesha","khan","is","good","girl")

"""

"""

def print_address(**kwargs):
  for key,value in kwargs.items():
    print(f"{key}:{value}")

print_address(street="chowmahalla",
              city="hyderabad",
              state="telangana",)    

"""

def shipping_label(*args,**kwargs):
  for arg in args:
     print(arg,end=" ")
  print()   

  if "apt" in kwargs:
     print(f"{kwargs.get('street')} {kwargs.get('Road')} {kwargs.get('apt')} ")
  else:
     print(f"{kwargs.get('street')} {kwargs.get('Road')}")



shipping_label("Aisha","khan",
               street="123",
               Road="Pimpiri",
              )  


