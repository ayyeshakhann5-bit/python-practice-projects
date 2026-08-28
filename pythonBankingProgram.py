def showBalance(balance):
  print(f"Your balance is ${balance:.2f}")

def deposit():
  amount=float(input("Enter an amount to be deposited:"))
  
  if amount<0:
    print("Enter valid amount")
    return 0
  else:
    return amount


def withdraw(balance):
  amount=float(input("Enter amount to be withdrawn:"))
  
  if amount<0:
    print("Enter withdraw amount greater than 0")
    return 0
  elif amount>balance:
    print("Insufficient Funds")
    return 0
  else:
    return amount
    
def main():
    balance=0
    isBalance=True
    while isBalance:
     print("Banking Program:")
     print("1.Show Balance")
     print("2.Deposit")
     print("3.Withdraw")
     print("4.Exit")
   
   
     choice=input("Enter your choice:")
   
     if choice=='1':
      showBalance(balance)
     
     elif choice=='2':
      balance+=deposit()
     
     elif choice=='3':
      balance-=withdraw(balance)
     
     elif choice=='4':
      isBalance=False
     
     else:
      print("This is not a valid choice")
     
    print("Thank you ! have a nice day!")     
    
    
if __name__=='__main__':
    main()


       
     
   
   