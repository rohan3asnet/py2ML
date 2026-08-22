questions={
    'What is the capital of Nepal?':{
        'A': 'New Delhi',
        'B': 'Kathmandu',
        'C': 'Pokhara',
        'D': 'Chitwan'
        
    }
}
answers={
    'What is the capital of Nepal?':'B'
}
for question,options in questions.items():
    print(f"{question}")
    for option,info in options.items():
        print(f"{option}.{info}")

user_choice=input("Your answer ").upper()

if user_choice == answers['What is the capital of Nepal?']:
    print("Correct")

else:
    print("Wrong")

