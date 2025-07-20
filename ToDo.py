# todo.py

tasks = []

def show_menu():
    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")

def add_task():
    task = input("Enter new task: ")
    tasks.append({"task": task, "done": False})
    print("Task added!")

def view_tasks():
    if not tasks:
        print("No tasks yet.")
        return
    for idx, t in enumerate(tasks):
        status = "✓" if t["done"] else "✗"
        print(f"{idx+1}. [{status}] {t['task']}")

def mark_done():
    view_tasks()
    index = int(input("Enter task number to mark as done: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        print("Marked as done!")
    else:
        print("Invalid task number.")

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")