from auth.authentication import Auth
from models.task import Task

def main():
    auth = Auth()
    
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            auth.register_user(username, password)
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = auth.login(username, password)
            
            if user:
                print("Welcome %s" % user.username)
                while True:
                    print("1. Add task")
                    print("2. View tasks")
                    print("3. Logout")
                    user_choice = input("Enter your choice: ")
                    
                    if user_choice == "1":
                        task = input("Enter title: ")
                        description = input("Enter description: ")
                        due_date = input("Enter due date in format 1990-01-01: ")
                        priority = input("Enter priority [Low, Medium, High]: ")
                        task = Task(title=task, description=description, due_date=due_date, priority=priority,assigned_user=user.username)
                        print(f"Task {task.title} added successfully.")
                        user.assign_task(task)
                        
                    elif user_choice == "2":
                        user.view_tasks()
                        
                    elif user_choice == "3":
                        print("Logging out...")
                        break
                    
        elif choice == "3":
            print("Exiting...")
            break
        
if __name__ == "__main__":
    main()
                        