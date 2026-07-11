# while loop runs as long as certain condition is true
count =1
while count <=5:
    print(count)
    count+=1

# letting user choose when to quit
prompt='\n tell me something  and i will say it back to you:'
prompt += '\n enter quit to end the program. '
message=""
while message != 'quit':
    message=input(prompt)
    print(message)

# we use flag as a signal to program
# flag= true raakhera program run garney ra 
# flag= false hudaa program stop huney, 
# flag= false chai kehi condition ley huney
# so yeso gardaa haami ley tyo set of conditions jasley flag=false
# banaauxa, teslai neatly organize garera raakhna sakinxa
prompt='\n tell me something  and i will say it back to you:'
prompt += '\n enter quit to end the program. '
flag = True
while flag:
    message=input(prompt)

    if message == 'quit':
        flag = False
    else:
        print(message)

# break allow to exit while loop immediately without running any remaining code in the loop
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    if city == 'quit':
            break
    else:
            print(f"I'd love to go to {city.title()}!")

# break ley k garxata, direct loop exit haanxa 
# tara continue ley beginning of the loop maa pathaauxa
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

#if you ever write an infinite while loop
# then you can exit from that state 
# by simple exiting the terminal which is displaying your output 
# or by pressing CTRL + C
# make sure at least one part of the program makes 
# loop's condition false or cause it to reach the break statement

#using a while loop with lists and dictionaries
# for loop doesnot allow you to modify the list
# but while loop allow you to collect, store and organize inputs
unread_books=['war and peace', 'Namesake', 'Siddartha', 'Dracula', 'Metamorphosis']
read_books=[]

while unread_books:
     current_book = unread_books.pop()

     print(f"Currently reading: {current_book.title()}")
     read_books.append(current_book)

print(f"\nThe following books have been completed:")
for read_book in read_books:
     print(read_book.title())

#filling a dictionary with user input
books={}
flag = True
while flag:
    name=input("\nWhat is your name? ")
    book=input("which book is your favourite? ")

    books[name]=book

    repeat=input("would somebody want to share information? (yes/no) ")
    if repeat == 'no':
        flag=False

print("\n*** Poll Results ***")
for name, book in books.items():
    print(f"{name} loves to read {book}.")
