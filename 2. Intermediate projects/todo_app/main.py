from task_manager.task_operation import add_task, remove_task, list_tasks, toggle_task
from task_manager.task_storage import save_tasks, load_tasks

def main():
    tasks = load_tasks()
    
    while True:
        print("\n--- To-do List Application ---")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Toggle Task Completion")
        print("5. Save and Quit")
        
        option = int(input("Enter your choice from 1 to 5:"))
        
        if option == 1:
            title = input("Enter your title: ")
            description = input("Enter your description (optional): ")
            tasks = add_task(tasks, title, description)
        elif option == 2:
            list_tasks(tasks)
            index = int(input("Enter the index of the task you want to remove: "))
            tasks = remove_task(tasks, index)
        elif option==3:
            list_tasks(tasks)
        elif option==4:
            list_tasks(tasks)
            index = int(input("Enter the index of the task to toggle: "))
            tasks = toggle_task(tasks, index)
        elif option==5:
            save_tasks(tasks)
            print("Your todo task has been saved.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()