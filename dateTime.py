import datetime

date=datetime.date(2025,1,2)
today=datetime.date.today()
time=datetime.time(12,30,0)
now=datetime.datetime.now()
now=now.strftime("%H:%M:%S %d-%m-%Y")
#print(now)

target_datetime=datetime.datetime(2020,1,2,12,30,0)

current_datetime=datetime.datetime.now()

if(current_datetime>target_datetime):
  print("Target date already passed")
else:
  print("Target date not already passed")  