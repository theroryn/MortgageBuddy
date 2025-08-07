# user.py
class User:
    def __init__(self, name, employee_id):
        self.name = name.strip()
        self.employee_id = employee_id.strip()

    def display_info(self):
        print(f"\nWelcome {self.name} (ID: {self.employee_id})")
