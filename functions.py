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

import time

def count(start,end):
    for x in range(start,end+1):
        print(x)
        time.sleep(0.2)
    print('DONE!')

count(0,5)    

  


