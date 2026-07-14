#function are generally designed to do a specific job
def greet_user():# this block is called function definition
    print("oe k xa?")

greet_user() #this is function call 

#passing information to a function
def greet_user(nickname):# nickname is parameter
    # parameter is a piece of information that function requires to do the job
    print(f"oe {nickname.upper()}, k gardaexas?")

greet_user('fuchhey')# fuchhey is argument

#positional arguments
# when you call a function, it must match each arguments with each parameters
def players_nickname(player, title):
    print(f"{player} is known as {title}")
#multiple function calls
players_nickname('Cristiano Ronaldo', 'GOAT')
players_nickname('Lionel Messi', 'FIFA Princess')
print('SUUUUIIIIIIIII')
# note: Order matters in positional arguments

#keyword arguments
# it is a name value pairs passed to a funciton
# it make sure there is no confusion
def players_nickname(player, title):
    print(f"{player} is known as {title}")
# now the order of keyword arguments donot matter
players_nickname(player='Cristiano Ronaldo', title='GOAT')
players_nickname(title='FIFA Princess', player='Lionel Messi')

#default value
# when argument is provided in function call, it used provided value
# if not then it uses default values
def acc_dueto_gravity(g=9.8):
    print(f'The value of acceleration due to gravity: {g}')

acc_dueto_gravity()

# example purpose only
# def example( name, age=19):
# for this function you can call it in variety of ways
# example('john')
# example('john', 18)
# example(name='john')
# example(name= 'john', age=20)
# example(age=20, name= 'john')

#return values
def area_of_circle(radius, pi=3.14):
    Area= pi* radius * radius
    return Area

radius=int(input("Enter the radius(cm) in integer to calculat Area: "))
print(f"Area of circle of radius {radius} is {area_of_circle(radius)} sq.cm.")

#returning a dictionary
def person_detail(fname, lname, age):
    person={
        'first name' : fname,
        'last name' : lname,
        'age' : age,
    }

    return person

info= person_detail("Rameshwor", "Yadav", 36)
print(info)

#using while loop with a funciton
def calculator(value1, value2):
    while True:
        print("choose which operation you want to perform\n")
        print(" + , - , / , * , q for quit")
        operator=input("input here: ")
        if operator == '+' :
            return value1 + value2
        elif operator == '*':
            return value1 * value2
        elif operator ==  '-':
            return value1 - value2
        elif operator == '/':
            return value1 / value2
        elif operator == 'q':
            break
ans=calculator(value1 =8, value2=2)
print(f"the answer is:{ans} ")
    
        
#passing a list
def book_list(books):
    for book in books:
        print(f"He wants to read {book.title()}")

booknames=['seto dharti', 'karnali blues', 'alikhit']
book_list(booknames)
# when you pass list to a function
# function can modify the list
# changes made are permanent
unread_books=['frankenstien', 'dracula', 'meditations','siddhartha']
completed_books=[]

def book_status(unread_books, completed_books):

    while unread_books:
        current_reads=unread_books.pop()
        print(f"currently reading: {current_reads.title()}")
        completed_books.append(current_reads)

def show_status(completed_books):
    print('\nAfter one month')
    print('I have completed following books')
    for completed_book in completed_books:
        print(completed_book.title())

book_status(unread_books, completed_books)
# book_status(unread_books[:], completed_books)
# this is done to prevent a funciton from modifying a list
# it sends a copy of existing list so that orginal remain unaffected
# only do this if you actually need it otherwise pass the orginal list
show_status(completed_books)

#passing an arbitrary number of arguments
def fav_books(*books):
    print(books)
# *books tells python to make tuples called books
# that tuple will contain all the values fav_books function recieves
# this is used when we dont know how many arguments function needs to accept
fav_books('Crime and Punishment')
fav_books('Kafka on the Shore', 'Norwegain Wood', 'The wind up bird chronicle')

def fav_books(*books):
    print('His favourites books are: ')
    for book in books:
        print(f"-{book}")

fav_books('Crime and Punishment')
fav_books('Kafka on the Shore', 'Norwegain Wood', 'The wind up bird chronicle')


#mixing positional and arbitrary arguments
# parameter that accepts arbitrary number of arguments must be placed at last
# python matches positinal and keyword arguments first
# and then collects remaining arguments in final parameter
def bookishh(page, *books):
    print(f"He read {page} pages of: ")
    for book in books:
         print(f"-{book}")

bookishh(20,'Crime and Punishment')
bookishh(30,'Kafka on the Shore', 'Norwegain Wood', 'The wind up bird chronicle')

#using arbitrary keyword arguments
def book_detail(author, bookname, **book_info):
    book_info['Author']=author
    book_info['Book']=bookname
    return book_info
# **book_info causes python to create a dictionary
# book_detail() first expects author and bookname 
# and accepts as many key-value pairs
book_information=book_detail('Murakami', 'The Wind up Bird Chronicle',
                             price=970,
                             genre='fiction',
                             publisher='Vintage')

print(book_information)

#importing an Entire Module

import pizza

pizza.make_pizza(16,'pepperoni')
pizza.make_pizza(12,'mushroom', 'pineapple', 'extra cheese')