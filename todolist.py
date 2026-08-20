tasks=[]

while True:
    print("===== TO-DO LIST =====")
    print("1. Add task\n2. View tasks\n3. Remove task \n4. Quit")
    user_choice=input("\nChoose an option: ")
    
    if user_choice == '1':

        task=input("Enter a task: ")
        tasks.append(task)

        print("Task added!\n")

    elif user_choice == '2':

        print("Your tasks:")
        if len(tasks)==0:
            print("Your Tasks list is empty.\n")
        else:
            for index, task in enumerate(tasks, start=1):
                
                print(f"{index}. {task}\n")

    elif user_choice == '3':
        remove_taks=int(input('Which task do you want to remove? '))
        del tasks[remove_taks-1]

        for index, task in enumerate(tasks, start=1):
                        
                        print(f"{index}. {task}\n")
        



    else:
        break

