# # while loop runs as long as certain condition is true
# count =1
# while count <=5:
#     print(count)
#     count+=1

# # letting user choose when to quit
# prompt='\n tell me something  and i will say it back to you:'
# prompt += '\n enter quit to end the program. '
# message=""
# while message != 'quit':
#     message=input(prompt)
#     print(message)

# # we use flag as a signal to program
# # flag= true raakhera program run garney ra 
# # flag= false hudaa program stop huney, 
# # flag= false chai kehi condition ley huney
# # so yeso gardaa haami ley tyo set of conditions jasley flag=false
# # banaauxa, teslai neatly organize garera raakhna sakinxa
# prompt='\n tell me something  and i will say it back to you:'
# prompt += '\n enter quit to end the program. '
# flag = True
# while flag:
#     message=input(prompt)

#     if message == 'quit':
#         flag = False
#     else:
#         print(message)

# exit while loop immediately without running any remaining code in the loop
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    if city == 'quit':
            break
    else:
            print(f"I'd love to go to {city.title()}!")