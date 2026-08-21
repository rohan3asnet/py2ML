tasks=[]
def show_menu():
    
    print("===== TO-DO LIST =====")
    print("1. Add task\n2. View tasks\n3. Remove task \n4. Quit")
    try:
        user_choice=int(input("\nChoose an option: "))
        return user_choice

    except ValueError:
        print("Invalid choice. Please try again")

def add_task():

    task=input("Enter a task: ")
    tasks.append(task)

    print("Task added!\n")

def view_task():

    print("Your tasks:")
    if len(tasks)==0:
        print("Your Tasks list is empty.\n")
    else:
        for index, task in enumerate(tasks, start=1):
            
            print(f"{index}. {task}\n")

def remove_task():

    remove_taks=int(input('Which task do you want to remove? '))
    try:
        del tasks[remove_taks-1]
        
        print("Task Removed!\n")
        print("Your remaining Tasks:\n")
        for index, task in enumerate(tasks, start=1):           
            print(f"{index}. {task}\n")

    except IndexError:
        print("Invalid Task number.")

while True:
    user_choice=show_menu()
    if user_choice ==1:
         add_task()

    elif user_choice ==2:
         view_task() 

    elif user_choice ==3:
         remove_task()

    elif user_choice ==4:
        break

    else:
        print("Not in the Option. Choose from the Option.")
        


# while True:
#     print("===== TO-DO LIST =====")
#     print("1. Add task\n2. View tasks\n3. Remove task \n4. Quit")
#     try:
#         user_choice=int(input("\nChoose an option: "))
        
#         if user_choice == 1:

#             task=input("Enter a task: ")
#             tasks.append(task)

#             print("Task added!\n")

#         elif user_choice == 2:

#             print("Your tasks:")
#             if len(tasks)==0:
#                 print("Your Tasks list is empty.\n")
#             else:
#                 for index, task in enumerate(tasks, start=1):
                    
#                     print(f"{index}. {task}\n")

#         elif user_choice == 3:
#             remove_taks=int(input('Which task do you want to remove? '))
#             try:
#                 del tasks[remove_taks-1]
                
#                 print("Task Removed!\n")
                
#                 for index, task in enumerate(tasks, start=1):           
#                     print(f"{index}. {task}\n")
#             except IndexError:
#                 print("Invalid Task number.")
#         elif user_choice == 4:
#             break

#         else:
#             print("Not in the Option. Choose from the Option.")
            
#     except ValueError:
#         print("Invalid choice. Please try again")    

