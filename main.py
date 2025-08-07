from User import User
from Calculator import Calculator

if __name__ == "__main__":
    print("=== MortgageBuddy - Sprint 1 ===")
    name = input("Enter your name: ")
    employee_id = input("Enter your employee ID: ")
    user = User(name, employee_id)

    app = Calculator(user)
    app.run()
