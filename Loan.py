class Loan:
    def __init__(self, principal, annual_rate, term_years, compounding_per_year=12):
        self.principal = principal
        self.annual_rate = annual_rate
        self.term_years = term_years
        self.compounding_per_year = compounding_per_year

    def total_due(self):
        r = self.annual_rate / 100
        n = self.compounding_per_year
        t = self.term_years
        return self.principal * (1 + r / n) ** (n * t)

    def total_interest(self):
        return self.total_due() - self.principal
