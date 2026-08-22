questions={
    'What is the capital of Nepal?':{
        'A': 'New Delhi',
        'B': 'Kathmandu',
        'C': 'Pokhara',
        'D': 'Chitwan'
        
    }

}

for question,answers in questions.items():
    print(f"{question}")
    for option,answer in answers.items():
        print(f"{option}.{answer}")

user_choice=input("Your answer ").upper()

