from User import User
from Calculator import Calculator

if __name__ == "__main__":
    print("=== MortgageBuddy - Sprint 2 ===")  # Updated version
    name = input("Enter your name: ")
    employee_id = input("Enter your employee ID: ")
    user = User(name, employee_id)

    app = Calculator(user)
    app.menu()  # Use menu-based CLI
