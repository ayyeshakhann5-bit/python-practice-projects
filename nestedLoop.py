rows=int(input("Enter the number of rows: "))
columns=int(input("Enter the number of columns: "))
symbol=input("Enter the symbol to print: ")
for i in range(rows):
    for j in range(columns):
        print(symbol, end="  ")
    print() 