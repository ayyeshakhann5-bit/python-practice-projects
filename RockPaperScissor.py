import random

options = ["rock", "paper", "scissors"]
running=True



while running:
   player=None
   computer = random.choice(options)
   while player not in options:
     player = input("Enter rock, paper, or scissors: ").lower()
     if player not in options:
      print("Invalid input. Please try again.")

   print(f"Player: {player}")
   print(f"Computer:{computer}")    


   if player == computer:
    print("It's a tie!")
   elif (player == "rock" and computer == "scissors"):
    print("You win! Rock beats scissors.")
   elif (player == "paper" and computer == "rock"):
    print("You win! Paper beats rock.")
   elif (player == "scissors" and computer == "paper"):
    print("You win! Scissors beats paper.")
   else:
    print("You lose! Better luck next time.")   

   play_again = input("Do you want to play again? (yes/no): ").lower()
   if play_again != "yes":
    running = False
    print("Thanks for playing! Goodbye.")