class Task:
    def __init__(self, title, description, completed=False):
        self.title = title
        self.description = description
        self.completed = completed
    
    def to_dict(self):
        return {
            "Title": self.title,
            "Description": self.description,
            "Completed": self.completed
        }