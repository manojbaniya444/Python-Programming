from models.user import User

class Auth:
    def __init__(self):
        self.users = []
        
    def register_user(self, username, password):
        for user in self.users:
            if user.username == username:
                raise Exception("Username already taken. Choose another.")
            
        new_user = User(username=username, password=password)
        self.users.append(new_user)
        print(f"User with username {username} registered successfully.")
            
    def login(self, username, passoword):
        for user in self.users:
            if user.username == username:
                if user.check_password(passoword):
                    return user
                else:
                    raise Exception("Invalid password.")
        raise Exception("User not found.")