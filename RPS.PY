import random

options =["rock","paper","scissor"]


while True:
    computer = random.choice(options).capitalize()
    player =input(" start the game choose (rock ,paper, scissor)").capitalize()
    if player not in options :
        print(f"{plyaer} is Ivalid input accept only (rock,paper or scissor)")
    
    if player == computer :
        print("you are tie "+"\n"+f"computer choice {computer}\nYour choice is {player}")
        
    elif (player == "Rock" and computer == "Scissor") or (player == "Paper" and computer =="Rock") or (player =="Scissor" and computer == "Paper"):
        print("you win")
        print(f"computer choice {computer}\nYour choice is {player}")

    else:
        print("you lose")
        print(f"computer choice {computer}\nYour choice is {player}")

    playing = input("continue playing (y/n) ").lower()
    
    if playing =="n":
        break
    