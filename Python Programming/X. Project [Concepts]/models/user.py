import bcrypt

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = self.hash_password(password)
        self.tasks = []
        
    def hash_password(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password)
    
    def assign_task(self, task):
        self.tasks.append(task)
    
    def view_tasks(self):
        for i, task in enumerate(self.tasks):
            # print("%d. %s" % (i + 1, task))
            print(f"Task {i + 1}. {task}")
    
    def __repr__(self):
        return f"User({self.username})"
    
if __name__ == "__main__":
    user = User("manoj444", "happy@123")
    user.assign_task("Complete this project.")
    user.assign_task("Learn langgraph.")
    
    user.view_tasks()
    print(user)