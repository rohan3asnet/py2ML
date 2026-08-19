tasks=[]

task=input("Enter a task: ")
tasks.append(task)

print("Task added!")

print("Your tasks:")
for index, task in enumerate(tasks):
    
    print(f"{index}. {task}")

