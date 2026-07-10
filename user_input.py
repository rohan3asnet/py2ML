# input() function pauses the program and waits for user input
# after recieving input, python assigns it to a variable
qNa = input('Where was Lord Gautam Buddha born?')
if qNa == 'Nepal':
    print('You have the right information.')
else:
    print('Well, you need some real education.')

#writing clear prompts
# add a space after the prompt so it separates users input and prompt
name=input('what is you name? ')
print(f'Hi! {name}')

# += it can be used to write multiline prompt
prompt='Everyone knows Mount Everest is the tallest Mountain on Earth.'
prompt+='But do you know where is it situated at? '
mt=input(prompt)
print(mt)

# input() takes everything as string 
# it is useful only to print the input
# so for numeric value we use int()
weight=input('what is your weight? \n')
weight=int(weight)
#OR
weight=int(input('what is your weight? \n'))
print(f"{weight}kg")
#just an example
no_of_people=int(input('How many people are in your dinner group? '))
if no_of_people <= 8:
    print('Your table is ready.')
else:
    print('you will have to wait for a table.')