"This class will represent tasks and their attributes"

from datetime import datetime

class StatusError(Exception):
    """Class for custom error handling"""
    def __init__(self, status):
        self.status = status
    def __str__(self):
        return f"Task status should be either Pending or Completed but got {self.status}"

class Task:
    def __init__(self, title, description, due_date, priority, assigned_user=None):
        self.title = title
        self.description = description
        self.due_date = datetime.strptime(due_date, r"%Y-%m-%d")
        self.priority = priority
        self.status = "Pending"
        self.assigned_user = assigned_user
        
    def mark_completed(self):
        self.status = "Completed"
        
    def change_status(self, status):
        if status not in ["Pending", "Completed"]:
            raise StatusError(status=status)
        self.status = status
        
    def __repr__(self):
        return f"Task({self.title}, {self.due_date}, {self.status})"
    
if __name__ == '__main__':
    task = Task("Backend project","This is the project in node js backend","2024-01-01", "High")
    task.change_status("Hello")
    print(task)