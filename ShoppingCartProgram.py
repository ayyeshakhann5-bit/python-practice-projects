Foods=[]
prices=[]
total=0

while True:
    food=input("Enter the food item in your cart(q to quit): ")
    if food.lower() == "q":
        break
    else:
        price=float(input(f"Enter the price of the {food}: $"))  
        Foods.append(food)
        prices.append(price)

      

print("\nYour shopping cart contains the following items:")
for food in Foods:
    print(food, end=" ")    

for price in prices:
    total+=price
print(f"\nYour total bill is: ${total:.2f}")





 


