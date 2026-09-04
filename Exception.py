try:
    number=int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
except ValueError:
    print("Error: Invalid input. Please enter a valid number")
except Exception:
  print("An unexpected error occurred")
finally:
  print("Execution completed")    
      