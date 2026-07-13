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