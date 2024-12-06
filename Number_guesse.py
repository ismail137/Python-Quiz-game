import random

num = random.randint(1,100)
minimum_guesses =7
guesses=[]
gameover=False

while not gameover:
    
    guesse = input("Enter your guesse between 1 and 100")

    if guesse.isdigit():
        guesse = int(guesse)
        if guesse<1 or guesse>100:
            print ("your input out of range")
            break
        if guesse>num:
            print(' too hight  please try again.')
            guesses.append(guesse)
        
        if guesse<num:
            print('too slow Try again')
            guesses.append(guesse)
        if len(guesses)==minimum_guesses:
            print(f"GAME OVER you have up of {minimum_guesses} tries and the correct num is {num}" )
            print(guesses)
            gameover=True
        
            print()
    else:
        print("invalid input your input must be number between 1 and 100")
    if guesse==num:
        print(f"YOU win good work your right you guess {guesse} and the computer number is {num}")
        guesses.append(guesse)
        print(f"you made it in {len(guesses)} tries "+'\n')
        print(guesses)

        gameover=True
