tasks = []

def add_task():
    task = input("Enter task name: ")
    tasks.append(task)
    print("Task added!")

def view_tasks():
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def delete_task():
    view_tasks()
    task_num = int(input("Enter task number to delete: "))
    if 1 <= task_num <= len(tasks):
        tasks.pop(task_num - 1)
        print("Task deleted!")
    else:
        print("Invalid task number.")

while True:
    print("\nTask Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Exiting Task Manager...")
        break
    else:
        print("Invalid choice. Try again.")
