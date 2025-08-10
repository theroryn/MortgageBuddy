class Loan:
    def __init__(self, principal, annual_rate, duration, compounding_per_year=12):
        self.principal = principal
        self.annual_rate = annual_rate
        self.duration = duration
        self.compounding_per_year = compounding_per_year

    def total_due(self):
        """Calculates total amount including interest payable."""
        r = self.annual_rate / 100
        n = self.compounding_per_year
        t = self.duration
        return self.principal * (1 + r / n) ** (n * t)

    def total_interest(self):
        """Calculates total interest payable."""
        return self.total_due() - self.principal