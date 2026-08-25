questions={
    'What is the capital of Nepal?':{
        'A': 'New Delhi',
        'B': 'Kathmandu',
        'C': 'Pokhara',
        'D': 'Chitwan'
        
    },
    'What is the capital of India?':{
            'A': 'New Delhi',
            'B': 'Kathmandu',
            'C': 'Pokhara',
            'D': 'Chitwan'
            
        }
}
answers={
    'What is the capital of Nepal?':'B',
    'What is the capital of India?':'A'

}

score=0
count=0

def display_question(question,options):
    print(f"{question}")
    for option,info in options.items():
        print(f"{option}.{info}")

def get_choice():
    user_choice=input("Your answer ").upper()
    return user_choice

def check_choice(question,user_choice):
    return user_choice == answers[question]


for question,options in questions.items():
    display_question(question, options)
    user_choice=get_choice()
    if check_choice(question,user_choice):
        print("Correct")
        score+=1
        count+=1
    else:
        print("Wrong")
        count+=1

print("=====Quiz Complete=====")
percentage=(score/count) *100
print(f"Score:{score}/{count} i.e. {percentage}%")
    


# for question,options in questions.items():
#     print(f"{question}")
#     for option,info in options.items():
#         print(f"{option}.{info}")

#     user_choice=input("Your answer ").upper()

#     ques=question
#     if user_choice == answers[ques]:
#         print("Correct")
#         score+=1
#         count+=1

#     else:
#         print("Wrong")
#         count+=1

# print("=====Quiz Complete=====")
# percentage=(score/count) *100
# print(f"Score:{score}/{count} i.e. {percentage}%")
