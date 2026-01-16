todo_list = []

while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        todo_list.append({"task": task, "done": False})
        print("Task added successfully!")

    elif choice == "2":
        if not todo_list:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(todo_list):
                status = "✔ Done" if task["done"] else "❌ Not Done"
                print(f"{i + 1}. {task['task']} - {status}")

    elif choice == "3":
        task_no = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= task_no < len(todo_list):
            todo_list[task_no]["done"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    elif choice == "4":
        print("Exiting To-Do List. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
