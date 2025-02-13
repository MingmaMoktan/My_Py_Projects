class Task:
    def __init__(self, title, description, completed=False):
        # Here completed=False will create the incomplete tasks while the user is adding the task. 
        self.title = title
        self.description = description
        self.completed = completed
    def todo_dict(self):
        return {
            "Title": self.title,
            "Description": self.description,
            "Complited": self.completed
        }
    