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
            for index, task in enumerate(tasks):
                
                print(f"{index}. {task}\n")

    elif user_choice == '3':
        print("remove task functions loading")

    else:
        break

