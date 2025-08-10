class User:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display_info(self):
        """Prints a short user introduction."""
        print(f"\n--- Welcome, {self.name} (ID: {self.employee_id}) ---")

    @staticmethod
    def load_users():
        """
        Loads authorized users from a text file.
        Note: To add or remove users, manually edit the 'users.txt' file.
        """
        users = []
        try:
            with open('users.txt', 'r') as file:
                for line in file:
                    name, employee_id = line.strip().split(',')
                    users.append({"name": name, "employee_id": employee_id})
        except FileNotFoundError:
            print("Error: users.txt not found. Please create it with at least one user.")
            exit()
        return users

    @staticmethod
    def authenticate():
        """Authenticates a user from the loaded list."""
        authorized_users = User.load_users()
        name = input("Enter your name: ")
        employee_id = input("Enter your employee ID: ")
        
        for auth_user in authorized_users:
            if auth_user["name"].lower() == name.lower() and auth_user["employee_id"] == employee_id:
                return User(name, employee_id)
        return None