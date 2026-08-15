import random

comp_num=random.randrange(1,100)

while True:
    user_num=int(input("Enter your guess: "))
    
    if comp_num > user_num:
        print("Go Higher ")
        continue

    elif comp_num < user_num:
        print("Go Lower")
        continue

    else:
        print("Correct")
        break


