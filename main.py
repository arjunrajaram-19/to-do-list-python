def menu():
    print("\n1. View Tasks")
    print("2. Add Task")
    print("3. Edit Task")
    print("4. Mark Task Done")
    print("5. Delete Task")
    print("6: Clear all Tasks")
    print("7. Exit")

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            lines = f.readlines()
        tasks = []
        for task in lines:
            tasks.append(task.strip())
        return tasks
    except:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        i=0
        while i<len(tasks):
            print(str(i+1)+"."+tasks[i])
            i+=1
       
def add_task(tasks):
    task=input("Enter new task: ")
    if task.strip()=="":
        print("Task cannot be empty")
        return
    due_date = input("Enter due date (YYYY-MM-DD): ")
    tasks.append("[ ] "+task+" | Due: "+due_date)
    print("Task added")

def edit_task(tasks):
    view_tasks(tasks)
    if not tasks:
        print("No tasks available.")
        return
    try:
        index=int(input("Enter task number to edit: "))-1
    except:
        print("Invalid input")
        return
    if 0<=index<len(tasks):
        old_task=tasks[index]
        status=old_task[0:3]
        new_text=input("Enter new task: ")
        if new_text.strip()== "":
            print("Task cannot be empty")
            return
        parts=old_task.split("| Due: ")
        if len(parts)>1:
            due=parts[1]
        else:
            due="No date"
        change_due=input("Change due date? (y/n): ")
        if change_due.lower()=="y":
            due=input("Enter new due date (YYYY-MM-DD): ")

        tasks[index]=status+new_text+" | Due: "+due
        save_tasks(tasks)
        print("Task updated")
    else:
        print("Invalid task number")

def clear_all_tasks(tasks):
    confirm = input("Are you sure you want to delete ALL tasks? (y/n): ")
    if confirm.lower()=="y":
        tasks.clear()
        save_tasks(tasks)
        print("All tasks deleted.")
    else:
        print("Cancelled.")

def mark_done(tasks):
    view_tasks(tasks)
    if not tasks:
        print("No tasks available.")
        return
    try:
        index = int(input("Enter task number: "))-1
    except:
        print("Invalid input")
        return
    if 0<=index<len(tasks):
        tasks[index]=tasks[index].replace("[ ]","[X]")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
       print("No tasks available.")
       return
    try:
        index = int(input("Enter task number to delete: "))-1
    except:
        print("Invalid input")
        return
    if 0<=index<len(tasks):
        tasks.pop(index)
        print("Task deleted")

tasks=load_tasks()
while True:
    menu()
    choice = input("Choose: ")
    if choice=="1":
        view_tasks(tasks)
    elif choice=="2":
        add_task(tasks)
    elif choice=="3":
        edit_task(tasks)
    elif choice=="4":
        mark_done(tasks)
    elif choice=="5":
        delete_task(tasks)
    elif choice=="6":
        clear_all_tasks(tasks)
    elif choice=="7":
        save_tasks(tasks)
        break
    else:
        print("Invalid choice")