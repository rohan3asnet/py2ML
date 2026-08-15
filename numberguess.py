import random

comp_num=random.randrange(1,100)
guess_count=0
while True:
    user_num=int(input("Enter your guess: "))
    guess_count+=1
    if comp_num > user_num:
        print("Go Higher ")
        continue

    elif comp_num < user_num:
        print("Go Lower")
        continue

    else:
        print("Correct")
        break

print(f"You got it in {guess_count} attemps")
