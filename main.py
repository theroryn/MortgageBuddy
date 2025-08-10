from User import User
from Calculator import Calculator

if __name__ == "__main__":
    print("=== MortgageBuddy - Final Version ===")
    
    # Authenticate the user
    user = User.authenticate()
    
    if user:
        print(f"\nAccess granted. Welcome, {user.name}!")
        app = Calculator(user)
        app.menu()
    else:
        print("\nAccess denied. Invalid name or employee ID.")