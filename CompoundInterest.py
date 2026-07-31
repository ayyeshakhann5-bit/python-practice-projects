
principle=0;
rate=0;
time=0;

while True:
 principle=float(input('Enter principal:'))

 if(principle<0):
  print("principle can't be less than zero")
 else:
  break 

while True:
 rate=float(input('Enter rate:'))

 if(rate<0):
  print("rate can't be less than zero")
 else:
  break  

while True:
 time=float(input('Enter time:'))

 if(time<0):
  print("time can't be less than zero")
 else:
  break 


total=principle*pow(1+rate/100,time)
print(f"Your balance after {time} is $:{total}")

    

