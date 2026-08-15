import random

comp_num=random.randrange(1,100)
guess_count=0
total_count=7
print("You have only 7 attempts")
while True:
    print(f"You have {total_count} attempts left.")
    guess_count+=1
    if total_count !=0:
        try:
            user_num=int(input("Enter your guess: "))
            if comp_num > user_num:
                print("Go Higher ")

            elif comp_num < user_num:
                print("Go Lower")

            else:
                print("#####Correct#####")
                print(f"You got it in {guess_count} attemps.")
                break
            total_count-=1
        except ValueError:
            print("Enter only Valid input i.e. Positive Interger.")
    else:
        print("Better Luck next Time.")
        break

