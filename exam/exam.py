# task manager

import json


class Task:
    def __init__(self, title):
        self.title = title
        self.status = "Pending"

    def to_dict(self):
        return {"title": self.title, "status": self.status}


def load():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except:
        return []

def save(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

tasks = load()

while True:
    print("1.Add 2.View 3.Complete 4.Delete 5.Exit")
    choice = input("Choose: ")

    if choice == "1":
        t = input("Task: ")
        task = Task(t)                 
        tasks.append(task.to_dict())   
        save(tasks)

    elif choice == "2":
        for i, t in enumerate(tasks):
            print(i+1, t["title"], t["status"])

    elif choice == "3":
        n = input("Number: ")
        if n.isdigit() and 0 < int(n) <= len(tasks):
            tasks[int(n)-1]["status"] = "Completed"
            save(tasks)

    elif choice == "4":
        n = input("Number: ")
        if n.isdigit() and 0 < int(n) <= len(tasks):
            tasks.pop(int(n)-1)
            save(tasks)

    elif choice == "5":
        break
    else:
        print("Invalid choice")