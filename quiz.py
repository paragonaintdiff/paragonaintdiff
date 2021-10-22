def new_game():
    
    guesses = []
    correct_guess = 0
    questions_num = 1

    for key in questions:
        print("_______________________________________________")
        print(key)
        for i in options[questions_num-1]:#To print respective option under each question...
            print(i)
        guess = input("Pls select one (A,B,C, or D) : ").upper()
        guesses.append(guess)
        #print(guess)
        questions_num += 1
        correct_guess += check_answer(questions.get(key),guess)
    
    display_score(correct_guess,guesses)
#------------------------------------------------------------
def check_answer(answer,guess):
        if guess==answer:
            print('Correct!')
            return 1
        else:
            print("Wrong! ")
            return 0
    
#------------------------------------------------------------
def display_score(correct_guess,guesses):
    print("xxxxxxxxxxxxxxxxxxxxxxxxx")
    print("Results")
    print("xxxxxxxxxxxxxxxxxxxxxxxxx")
    
    print("Answers :", end="")
    for i in questions:
        print(questions.get(i) ,end=" ")
    print()

    print("Guesses :", end=" ")
    for i in guesses:
        print(i ,end=" ")
    
    score = (correct_guess/len(questions))*100
    print()
    print("Your score is "+str(score)+"%")
    print()
    if score >=75:
        print("Congratulations!")
    else:
        print("Too Bad!")

#------------------------------------------------------------   
def play_again():
    
    response = input("Play again? (yes/no) : ").upper()
    if response == "YES":
        return True
    else:
        return False

#------------------------------------------------------------

questions = { 
"Who created Python ?":"A",
"When was Python created ?":"B",
"Python is tributed to which comedy group ?":"A",
"Do Mthc loves me ?":"B"
}
options = [
["A. Guido van Rossun ","B. Elon Musk ", "C. Bill Gates ","D. Mark Zuckerburg ",],
["A. 1989 ", "B. 1991", "C. 2001", "D. 2010"],
["A. Lonley Island", "B. Smosh ", "C. Monty Python", "D. SNL"],
["A. Prolly", "B. Never in a million years", "C. Yes", "D. Idk"]
]

new_game()#To begin a new game  

while play_again():

    new_game()

print("Byeeeeeeeeeeeeeeeeeee.....")
