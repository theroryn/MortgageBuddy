# Task Tracker Sprint Log: Sprint 1

## Sprint goal
To implement the core object-oriented structure of the MortgageBuddy app, including:
- Definition of the `User`, `Loan`, and `Calculator` classes with attributes and `__init__` methods
- Implement `User.display_info()` to show user name and ID
- Implement compound interest methods in `Loan` class: `total_due()` and `total_interest()`
- Build `Calculator.run()` method to prompt user input and display results
- Add input validation to handle incorrect types and negative values
- Manual testing via `main.py`
- Internal documentation and preparation for future extension

---

## Tasks completed
- Created `user.py` containing the `User` class with attributes: `name`, `employee_id`, and method `display_info()`
- Created `loan.py` containing the `Loan` class with attributes: `principal`, `rate`, `duration`, `compounding_per_year` and methods `total_due()` and `total_interest()`
- Created `calculator.py` containing the `Calculator` class with the `user` attribute and a `run()` method that:
  - Prompts for loan input values
  - Handles input errors
  - Instantiates a `Loan` object and displays results
- Created `main.py` to coordinate program execution and act as the CLI entry point
- Added input validation for numeric and non-negative values using `try/except` blocks
- Tested program behavior using known values and edge cases (e.g. 0% interest, negative inputs)
- Documented all classes and methods using Python docstrings
- Drafted `README.md` with system overview, usage instructions, and setup requirements
- Created SDS sections for class architecture, assumptions, and planned sprint features
- Added inline TODO comments for future enhancements (e.g., authentication, file saving)

---

## Resources used
- Python documentation (classes, float formatting, exception handling)
- ChatGPT for:
  - Validating compound interest logic
  - Providing class design suggestions
  - Supporting error handling patterns
- SDS outline template provided by the course for structure

---

## Testing log

| Test case                   | Input                                          | Expected outcome                      | Actual outcome | Notes                          |
|-----------------------------|------------------------------------------------|----------------------------------------|----------------|--------------------------------|
| Display user info           | Name + ID                                      | Printed welcome message                | Confirmed      | Simple print()                 |
| Create loan object          | 100000, 5.0, 30 years, 12 compounding          | Object created with correct values     | Confirmed      | Constructor handled types      |
| Compound interest - normal  | 100000 @ 5% for 30 years, monthly              | Matches spreadsheet output             | Confirmed      | Matches online calculator      |
| Compound interest - 0 rate  | 100000 @ 0% for 10 years                       | Total due = 100000                     | Confirmed      | Correct edge case              |
| Input validation            | Non-numeric or negative inputs                 | Caught and re-prompted                 | Confirmed      | Handled with try/except        |
| Output formatting           | Calculation results                            | 2 decimal places, labeled              | Confirmed      | Matches design expectations    |
| User flow (main.py)         | Full run from entry to output                  | Program runs end-to-end                | Confirmed      | Simple CLI achieved            |

---

## Version control
- Git repository initialized locally and on GitHub
- `user.py`, `loan.py`, `calculator.py`, and `main.py`added
- Commits made for each major class and test milestone
- `.gitignore` configured to exclude cache, environment files
- Pushed to a private GitHub repository using VS-Code Source Control

---

## Reflections
- Using OOP from the start made the code modular and easy to test
- Having a default compounding value simplified user input while staying realistic
- Input validation and manual testing confirmed that logic is robust for common scenarios
- The program is ready to be extended with features like saving files, menus, and user authentication
- Communication between the `User`, `Loan`, and `Calculator` classes worked well, requiring minimal glue code

---

## Notes for next sprint
- Implement file saving and loading of loan sessions (JSON or text format)
- Introduce a menu-based CLI to improve user interaction
- Explore adding a basic user authentication check
- Write unit tests for `Loan` and validation logic using `unittest`
- Start refining user prompts and output layout for professionalism
