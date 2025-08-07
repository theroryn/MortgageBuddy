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
