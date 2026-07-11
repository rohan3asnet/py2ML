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
