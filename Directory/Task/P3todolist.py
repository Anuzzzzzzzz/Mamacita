import json
from datetime import datetime

FILE = "tasks.json"

# Load tasks from file
try:
    with open(FILE, "r") as f:
        tasks = json.load(f)
except FileNotFoundError:
    tasks = []

while True:
    print("\n--- TO DO LIST ---")
    print("1. Add task")
    print("2. Show tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Stats")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":
        title = input("Task name: ")
        priority = input("Priority (High/Medium/Low): ")
        due_date = input("Due date (YYYY-MM-DD): ")
        task = {
            "title": title,
            "priority": priority,
            "due_date": due_date,
            "done": False,
            "created": datetime.now().strftime("%Y-%m-%d")
        }
        tasks.append(task)
        with open(FILE, "w") as f:
            json.dump(tasks, f, indent=4)
        print("Task added ✅")

    elif choice == "2":
        if not tasks:
            print("No tasks found.")
        else:
            for i, t in enumerate(tasks, start=1):
                status = "Done" if t["done"] else "Pending"
                print(f"{i}. {t['title']} | {status} | {t['priority']} | Due: {t['due_date']}")

    elif choice == "3":
        for i, t in enumerate(tasks, start=1):
            status = "Done" if t["done"] else "Pending"
            print(f"{i}. {t['title']} | {status}")
        num = int(input("Task number to complete: ")) - 1
        if 0 <= num < len(tasks):
            tasks[num]["done"] = True
            with open(FILE, "w") as f:
                json.dump(tasks, f, indent=4)
            print("Task completed 🎉")

    elif choice == "4":
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t['title']}")
        num = int(input("Task number to delete: ")) - 1
        if 0 <= num < len(tasks):
            tasks.pop(num)
            with open(FILE, "w") as f:
                json.dump(tasks, f, indent=4)
            print("Task deleted 🗑️")

    elif choice == "5":
        total = len(tasks)
        completed = sum(1 for t in tasks if t["done"])
        pending = total - completed
        print(f"Total tasks: {total} | Completed: {completed} | Pending: {pending}")

    elif choice == "6":
        print("Bye 👋")
        break

    else:
        print("Invalid choice")
