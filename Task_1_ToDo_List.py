tasks = []

print("Welcome to To-Do List Application")

while True:
    print("\nChoose an option:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter task name: ")
        tasks.append(task)
        print("Task added successfully.")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")
            try:
                num = int(input("Enter task number to remove: "))
                if num < 1 or num > len(tasks):
                    print("Invalid task number.")
                else:
                    removed_task = tasks.pop(num - 1)
                    print(f"Removed task: {removed_task}")
            except:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Exiting application. Thank you!")
        break

    else:
        print("Invalid choice. Please select between 1 to 4.")
