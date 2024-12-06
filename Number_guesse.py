import random

num = random.randint(1,100)
minimum_guesses =7
guesses=[]
gameover=False

while not gameover:
    guesse = int(input("Enter your guesed numb between 1 to 100     "    ))
    print()
    if guesse != num:
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
    if guesse==num:
        print(f"YOU win good work your right you guess {guesse} and the computer number is {num}")
        guesses.append(guesse)
        print(f"you made it in {len(guesses)} tries "+'\n')
        print(guesses)

        gameover=True
       