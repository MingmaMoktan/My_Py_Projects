from .task import Task

def add_task(tasks, title, description=""): # Here description = "" is setting the default value the empty string if no description is given.
    new_task = Task(title, description)
    tasks.append(new_task)
    return tasks

def remove_task(tasks, index):
    if 