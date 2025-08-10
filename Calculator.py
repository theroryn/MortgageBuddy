from Loan import Loan

class Calculator:
    def __init__(self, user):
        self.user = user

    # Basic validation helpers 
    def get_positive_float(self, prompt):
        while True:
            try:
                value = float(input(prompt))
                if value <= 0:
                    print("Error: Value must be greater than zero.")
                    continue
                return value
            except ValueError:
                print("Error: Please enter a numeric value.")

    def get_non_negative_float(self, prompt):
        while True:
            try:
                value = float(input(prompt))
                if value < 0:
                    print("Error: Value cannot be negative.")
                    continue
                return value
            except ValueError:
                print("Error: Please enter a numeric value.")

    def get_positive_int(self, prompt):
        while True:
            try:
                value = int(input(prompt))
                if value <= 0:
                    print("Error: Please enter a positive whole number.")
                    continue
                return value
            except ValueError:
                print("Error: Please enter a whole number.")

    # Save loan data to text file
    def save_loan(self, loan):
        with open("loan_data.txt", "w") as f:
            f.write(f"{loan.principal},{loan.annual_rate},{loan.term_years},{loan.compounding_per_year}")
        print("Loan data saved successfully to loan_data.txt")

    # Load loan data from text file
    def load_loan(self):
        try:
            with open("loan_data.txt", "r") as f:
                data = f.read().strip().split(",")
                principal = float(data[0])
                annual_rate = float(data[1])
                term_years = float(data[2])
                compounding_per_year = int(data[3])
                return Loan(principal, annual_rate, term_years, compounding_per_year)
        except FileNotFoundError:
            print("No saved loan data found.")
            return None
        except (ValueError, IndexError):
            print("Error reading loan data. The file may be corrupted.")
            return None

    # Menu-based CLI loop
    def menu(self):
        while True:
            print("\n--- MortgageBuddy Menu ---")
            print("1. Create new loan calculation")
            print("2. View last saved loan")
            print("3. Exit")
            choice = input("Select an option: ")

            if choice == "1":
                self.run()
            elif choice == "2":
                loan = self.load_loan()
                if loan:
                    print(f"\nAmount Due After Interest: ${loan.total_due():.2f}")
                    print(f"Total Interest Accrued:   ${loan.total_interest():.2f}")
            elif choice == "3":
                print("Exiting MortgageBuddy. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def run(self):
        self.user.display_info()
        print("\n--- Mortgage Compound Interest Calculator ---")

        principal = self.get_positive_float("Enter principal loan amount ($): ")
        rate = self.get_non_negative_float("Enter annual interest rate (%): ")
        term = self.get_positive_float("Enter loan term (years): ")
        compounding = self.get_positive_int("Enter compounding frequency per year (e.g., 12 for monthly): ")

        loan = Loan(principal, rate, term, compounding)

        print("\n--- Calculation Results ---")
        print(f"Amount Due After Interest: ${loan.total_due():.2f}")
        print(f"Total Interest Accrued:   ${loan.total_interest():.2f}")

        save_choice = input("Would you like to save this loan? (y/n): ").strip().lower()
        if save_choice == "y":
            self.save_loan(loan)
