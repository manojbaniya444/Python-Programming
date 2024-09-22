import json
from models.user import User
from models.task import Task

class Database:
    def __init__(self):
        self.users = []
        self.tasks = []
        
    def add_user(self, user: User):
        self.users.append(user)
        
    def add_ask(self, task: Task):
        self.tasks.append(task)
    
    def save_to_file(self, file_path="data.json"):
        data = {
            "users": [user.__dict__ for user in self.users],
            "tasks": [task.__dict__ for task in self.tasks]
        }
        
        with open(file_path, "w") as myfile:
            json.dump(data, myfile, indent=7)
            
    def load_from_file(self, file_path="data.json"):
        with open(file_path, "r") as myfile:
            data = json.load(myfile)
        self.users = data.get("user", [])
        self.tasks = data.get("tasks", [])