cart=[]
prices=[]
totale =0

while True:
    food=input("What you want to buy today")
    if food.lower()=="q":
        break
    else :
       cost = float(input("How much is cost you?"))
       cart.append(food)
       prices.append(cost)

for food in cart:
    print(food, end="| ")

for price in prices:
    totale +=price   

print(f"You have to pay {totale}")    