#TO DO LIST
tasks = []
while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")
    choice = input("Choose an option (1-4): ")
    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print(" Task added!")
    elif choice == "2":
        if not tasks:
            print(" No tasks found.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")
    elif choice == "3":
        if not tasks:
            print(" No tasks to delete.")
        else:
            task_num = int(input("Enter task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f" Removed: {removed}")
            else:
                print(" Invalid task number.")
    elif choice == "4":
        print(" Exiting To-Do App. Bye!")
        break
    else:
        print(" Invalid choice. Try again.")
