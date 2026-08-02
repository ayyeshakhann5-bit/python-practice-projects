menu={"pizza":3.40,
      "hot dog":2.50,
      "hamburger":3.00,
      "nachos":2.75,
      "soda":1.50,
      "water":1.00}

cart=[]
total=0

print("---Welcome to the Concession Stand! Here is our menu:---")

for key ,value in menu.items():
    print(f"{key:10}: ${value:.2f}")

print("---------------------------------------------------------")
while True:
    item=input("Please enter the item you would like to order (or type 'q' to finish): ").lower()
    if item == 'q':
        break
    elif menu.get(item) is not None:
        cart.append(item)


print("--------""Your Order Summary:--------")
for item in cart:
    total+=menu.get(item)
    print(item,end=", ")     

print()
print(f"Your total is: ${total:.2f}")

    




