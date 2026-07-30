unit=input("Is this temperature in C or F:")
temp=(float)(input("Enter the temp:"))

if unit == "C":
  temp=round((9*temp)/5+32,1)
  print(f"The temp in fahrenheit is: {temp}°F")
elif unit == "F":
  temp=round((temp-32)*5/9,1)
  print(f"The temp in Celsius is: {temp}°C")
else:
  print(f"Your {unit} temp is invalid unit of measurement")
