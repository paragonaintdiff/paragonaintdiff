import random

while True:

    choices = [ "rock", "paper", "choices"]

    computer = random.choice(choices)

   
    
    player = None
    while not player in choices:
        player = input("rock , paper , or gun ? : ").lower()

    if player == computer:
        print("Computer", computer)  
        print(" You ", player )
        print(" Tie! ")
    elif player == "paper":
        if computer == "rock":   
            print("Computer", computer)  
            print(" You ", player )
            print(" You win! ")
        if computer == "gun":
            print("Computer", computer)  
            print(" You ", player )
            print(" You lose! ")
    elif player == "rock":
        if computer == "paper":   
            print("Computer", computer)  
            print(" You ", player )
            print(" You lose! ")
        if computer == "gun":
            print("Computer", computer)  
            print(" You ", player )
            print(" You Win! ")
    elif player == "gun":
        if computer == "rock":   
            print("Computer", computer)  
            print(" You ", player )
            print(" You lose! ")
        if computer == "paper":
            print("Computer", computer)  
            print(" You ", player )
            print(" You Win! ")
    
# yes_or_no = ["yes","no"]
# player = None
# while  not player in yes_or_no:
    player = (input("Play agin? (yes/no) : ")).lower()
    if player != "yes":
        break
print("Bye!"*2)