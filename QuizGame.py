questions=(("How many elements are there in a Periodic Table?"),
           ("What is the capital of France?"),
           ("What is the largest planet in our solar system?"),
           ("Who painted the Mona Lisa?"),
           ("What is the chemical symbol for gold?"))

options=(("A. 118","B. 120","C. 115","D. 110"),
         ("A. Berlin","B. Madrid","C. Paris","D. Rome"),
         ("A. Earth","B. Jupiter","C. Saturn","D. Mars"),
         ("A. Vincent van Gogh","B. Pablo Picasso","C. Leonardo da Vinci"," D. Michelangelo"),
         ("A. Au","B. Ag","C. Fe","D. Hg"))


answers=("A","C","B","C","A")
guesses=[]
score=0
question_num=0




for question in questions:
    print("------------------------------")
    print(question)
    for option in options[question_num]:
     print(option)
    guess=input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess==answers[question_num]:
        print("CORRECT!")
        score+=1
    else:
        print("WRONG!")
        print(f"{answers[question_num]} is the correct answer.")
    question_num+=1
print()  


print("------------------------------")
print("RESULTS")
print("------------------------------")
print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()
print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score_percentage=int(score/len(questions)*100)
print(f"Your score is: {score_percentage}%")