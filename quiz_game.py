questions={
    'What is the capital of Nepal?':{
        "options":{
            'A': 'New Delhi',
            'B': 'Kathmandu',
            'C': 'Pokhara',
            'D': 'Chitwan'
        },
        'correct_answer':'B'
    },
        
    
    'What is the capital of India?':{
        'options':{
            'A': 'New Delhi',
            'B': 'Kathmandu',
            'C': 'Pokhara',
            'D': 'Chitwan'
        },
        'correct_answer':'A'
            
        }
}
# answers={
#     'What is the capital of Nepal?':'B',
#     'What is the capital of India?':'A'

# }

score=0

def display_question(question,options):
    print(f"{question}")
    for option,info in options.items():
        print(f"{option}.{info}")

def get_choice():
    while True:
        user_choice=input("Your answer ").upper()
        if user_choice not in ['A','B','C','D']:
            print('Not in option. Input either A, B, C or D')
            continue
        else:
            return user_choice
        

def check_choice(data,user_choice):
    return user_choice == data['correct_answer']


for question,data in questions.items():
    display_question(question, data["options"])
    user_choice=get_choice()
    if check_choice(data,user_choice):
        print("Correct")
        score+=1
    else:
        print("Wrong")
        

print("=====Quiz Complete=====")
percentage=(score/len(questions)) *100
print(f"Score:{score}/{len(questions)} i.e. {percentage}%")
    


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
