from .task import Task

def add_task(tasks, title, description=""):
    new_task = Task(title, description)
    task_id = len(tasks) + 1
    tasks[task_id] = new_task
    return tasks

def remove_task(tasks, task_id):
    if task_id in tasks:
        removed_task = tasks.pop(task_id)
        print(f"Task '{removed_task.title}' has been removed.")
    else:
        print(f"Task with ID {task_id} not found.")
    return tasks

def list_tasks(tasks):
    for task_id, task in tasks.items():
        status = "✓" if task.completed else " "
        print(f"{task_id}. [{status}] {task.title}")
        if task.description:
            print(f"   Description: {task.description}")

def toggle_task(tasks, task_id):
    if task_id in tasks:
        tasks[task_id].completed = not tasks[task_id].completed
        status = "completed" if tasks[task_id].completed else "not completed"
        print(f"Task '{tasks[task_id].title}' is now {status}.")
    else:
        print(f"Task with ID {task_id} not found.")
    return tasks