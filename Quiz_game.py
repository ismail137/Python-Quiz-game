questions =("How th element in the periodic table?",
            "Which animals lays the largest eggs",
            "what is the most abundant gas in the atmesphere",
            "How many bones are in the human body",
            "Which the planet in the solar systme is the hottest?:")

options = (("A 116","B 117","C 118","D 119"),
          ("A Whale","B Crocodile","C Elephant","D Otrish"),
          ("A Nitrogen","B Oxygen","C Carbon-Dioxide","D Hydrogen"),
          ("A 206","B 207","C 208","D 209"),
          ("A  mercury","B Venus","C Earth","D Mars"),
          ("light"))

answers =("C","D","A","A","B")

guesses=[]
score =0
question_num=0
print(f"You have {len(questions)} questions  to solve in this quiz Game")
for question in questions:
    
    print("--------------------------------------------")
    print(f"THE QUESTION N*{question_num +1}")
    print(question)
    for option in options[question_num]:
        print(option)
    print("The next question will appear the your answer")  
    guesse = input("Please type your answer here A.B.C.D ").upper()
    guesses.append(guesse)
   
    if guesse.lower() =="q":
        break
    if guesse == answers[question_num]:
        print(f"Good work your {answers[question_num]} is correct")
        score+=1
        print(score)
    else:
        print(f"Sorry you {guesse} is incorrect\nThe correct annswer is: {answers[question_num]}")

    question_num+=1


for answer in answers:
    print(answer,end="|")
print()
for guess in guesses:
    print(guess , end="|")
progress=int((score/len(answers))*100)
match progress:
    case x if x<10 :
        print(f"progress {progress}% I'm sorry you loose you answered nothon")
    case x if x>=10 and x<40:
        print(f"Progress {progress}% you loosed  your score is too low ")
    case x if x>= 40 and x<=60:
        print(f"Progress {progress}% you do well continuew next time")
    case x if x>60 and x<100:
        print(f"progress {progress}% your on the edge to ace the game ")
    case 100 :
        print(f"Progress {progress}% :you are a hero ")