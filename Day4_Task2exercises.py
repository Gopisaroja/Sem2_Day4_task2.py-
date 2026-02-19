# To do app
task = []

while True:
    print("To do app:")
    choice = input("Enter the choice:\n1.Add a task.\n2.View the task.\n3.Delete a task.\n4.Exit.\n")
    
    if choice == "1":
        task1 = input("Enter task:")
        task.append(task1)
        print("Tasks added successfully!\n")
        
    elif choice == "2":
        if len(task) == 0:
            print("No tasks available, add a task to show up!")
        else:
            print("Tasks are:")
            for i in range(len(task)):
                print(i + 1, ".", task[i])
                
    elif choice == "3":
        if len(task) == 0:
            print("No tasks available, add a task to show up!")
        else:
            delete =int(input("Enter the task number to delete:"))
            length=len(task)
            if 1<=delete<=length:
            	task.pop(delete-1)
            	print("Task deleted successfully!\n","Available tasks:",task)
            else:
            	print("Invalid task number!")
    elif choice=="4":
        print("Exiting....")    
        break
    else:
        print("Invalid choice!")		   	         		