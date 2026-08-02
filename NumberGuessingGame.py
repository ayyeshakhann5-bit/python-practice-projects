import random

lowest=1
highest=100

guesses=0

isRunning=True

answer=random.randint(lowest, highest)

print("Welcome to the Number Guessing Game!")

print(f"Select a number between {lowest} and {highest}")

guess=(input("Enter your guess: "))

while isRunning:
  if guess.isdigit():
     guess=int(guess)
     guesses+=1
     if guess<lowest or guess>highest:
       print("Your guess is out of range.")
       print(f"Please enter a number between {lowest} and {highest}")
       guess=(input("Enter your guess: "))

     elif guess<answer:
       print("Your guess is too low.")
       guess=(input("Enter your guess: ")) 
     elif guess>answer:
       print("Your guess is too high.")
       guess=(input("Enter your guess: "))
     else:
       print(f"Congratulations! You guessed the number {answer} in {guesses} guesses.")
       isRunning=False  
    
       
  else:
    print("Please enter a valid number.")
    guess=int(input("Enter your guess: "))
    


