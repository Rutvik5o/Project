todo_list = []

def show_menu():
    print("\nTo-Do list options")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit\n--------------------\n")


def view_tasks():
    if not todo_list:
        print("No Tasks yet")
    else:
        print("\nYour Tasks:")
        for idx,task in enumerate(todo_list,start = 1):
            print(f"{idx}. {task}")


def add_task():
    task = input("Enter the task : ")
    todo_list.append(task)
    print("Task Added")

def remove_task():
    view_tasks()
    try:
        index = int(input("Enter task number to remove->")) -1 
        removed = todo_list.pop(index)
        print(f"Removed: {removed}")
    except(IndexError,ValueError):
        print("\n--------------\nInvalid Task number\n--------------\n")


while True:
    show_menu()
    choice = input("Choose an option(1-4):")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Good Bye!")
        break
    else:
        print("Invalid Option")

