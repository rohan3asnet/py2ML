print("===== TO-DO LIST =====")
print("1. Add task\n2. View tasks\n3. Remove task \n4. Quit")
user_choice=input("\nChoose an option: ")

if user_choice == '1':

    tasks=[]

    task=input("Enter a task: ")
    tasks.append(task)

    print("Task added!")

elif user_choice == '2':

    print("Your tasks:")
    for index, task in enumerate(tasks):
        
        print(f"{index}. {task}")

elif user_choice == '3':
    print("remove task functions loading")

else:
    print("quit function loading")

