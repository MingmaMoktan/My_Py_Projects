import json
from .task import Task

def save_tasks(tasks):
    serializable_tasks = {str(task_id): task.to_dict() for task_id, task in tasks.items()}
    with open("tasks.json", "w") as file:
        json.dump(serializable_tasks, file)

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            loaded_tasks = json.load(file)
            return {int(task_id): Task(task_data["Title"], task_data["Description"], task_data["Completed"]) 
                    for task_id, task_data in loaded_tasks.items()}
    except FileNotFoundError:
        return {}