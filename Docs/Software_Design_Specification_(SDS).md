# Software Design Specification (SDS)

## Project name
Mortgage Buddy

## Version
v1.0 – Initial system design (covers all planned features across sprints)

## Overview
Mortgage Buddy is a command-line application that enables loan specialists to calculate. It is developed using object-oriented design and an agile workflow. The app is built incrementally over several sprints, each delivering a functional stage of development. The main feature of the application is to calculate a principal and interest loan, with the ability to choose the capital, interest rate, compounding frequency, and loan duration.

The system design outlined here covers the full project scope, even though features will be implemented gradually over time.


## User Stories

1. **As a loan officer**, I want to enter a customer's loan details (principal, interest rate, term, compounding frequency), so that I can calculate the total repayment and interest due.

2. **As a bank employee**, I want to see clear calculation results in the terminal, so that I can quickly communicate figures to clients or record them manually.

3. **As a bank staff member**, I want input validation and helpful error messages, so that I don’t waste time troubleshooting entry mistakes.

4. **As a loan officer**, I want the software to save my session results to a file, so that I can retrieve or report them later if needed.

5. **As a team lead**, I want users to be authenticated before using the tool, so that usage can be restricted to authorized personnel.

6. **As a bank auditor**, I want loan calculations to be consistent and traceable, so that we can comply with financial regulations.

7. **As a future developer**, I want the codebase to be modular and testable, so that I can maintain and expand it with ease.

## Use Cases

### Use Case 1: Calculate Mortgage Compound Interest

**Actor:** Loan Officer  
**Precondition:** User is running the Mortgage Buddy program  
**Steps:**
1. User enters name and employee ID  
2. User is welcomed by the program  
3. User is prompted to input loan details:
   - Principal
   - Interest rate
   - Loan duration
   - Compounding frequency
4. Program calculates total due and interest
5. Results are displayed in a readable format

**Postcondition:** Loan officer sees results and can relay them to a customer

---

### Use Case 2: Input Validation

**Actor:** Any user  
**Precondition:** Calculator is running  
**Steps:**
1. User inputs loan parameters  
2. If input is invalid (e.g. letters in number fields), the program gives an error message  
3. Program re-prompts the user

**Postcondition:** Program prevents bad input and ensures valid calculations

---

### Use Case 3: Save Loan Session (Optional)

**Actor:** Loan Officer  
**Precondition:** Loan calculation is complete  
**Steps:**
1. Program offers option to save session
2. If accepted, calculation and user data are saved to a file

**Postcondition:** Data is persisted for later access

---

### Use Case 4: Authenticate Employee (Optional – Sprint 3)

**Actor:** Bank employee  
**Precondition:** Program has loaded an allowed users list  
**Steps:**
1. User enters name and ID  
2. Program checks against authorized users  
3. If valid, user is allowed access; else denied

**Postcondition:** Access is secured



## System architecture
The system consists of three main classes:

- `User`: Represents the 'login' process which handles the attributes of the users name and employee ID.
- `Loan`: Manages all the calculations required to display the total loan amount and interest payable.

- `Calculator`: A front that aqcuires all necessary information from users in order to calculate and display loan calculation results

The program is designed for terminal-based use and avoids GUI dependencies. Each sprint builds on the existing functionality.

## Class descriptions

### User

| Attribute       | Type     | Description                                 |
|----------------|----------|---------------------------------------------|
| `name`        | `str`    | Name of employee(user) that is currently accessing software |
| `employee_id`  | `str`    | An employee ID that can include a mix on letters and numbers |


| Method              | Description                                |
|---------------------|--------------------------------------------|
| `display_info()`   | Prints a short user introduction               |

### Loan

| Attribute | Type        | Description                                |
|-----------|-------------|--------------------------------------------|
| `principal`   | `float`| Loan amount             |
| `rate`   | `float`| Interest rate per period             |
| `duration`   | `float`| Length of loan             |
| `compounding_per_year`   | `float`| compounding frequency per year             |

| Method                    | Description                                         |
|---------------------------|-----------------------------------------------------|
| `total_due()`          | Calculates total amount including interest payable                       |
| `total_interest()`            | calculates interest payable                       |



### Calculator

| Attribute | Type        | Description                                |
|-----------|-------------|--------------------------------------------|
| `user`   | `str`| user id and name             |

| Method                    | Description                                         |
|---------------------------|-----------------------------------------------------|
| `run()`          | runs main process, being able to handle user '1 D 10 T' errors                       |



## Assumptions and constraints
- The application runs in a command-line interface (CLI) only.
- All data is stored in memory initially; persistence will be added in later sprints.
- Maximum loan amount is calculated; this will be added in later sprints

## Feature Backlog 


### Core Features (Sprint 1 – MVP)

| Feature                | Description                                                             | Linked User Stories |
|------------------------|-------------------------------------------------------------------------|----------------------|
| Class structure (OOP)  | Create `User`, `Loan`, and `Calculator` classes with attributes          | US07                 |
| Loan calculation       | Implement `total_due()` and `total_interest()` using compound interest  | US01, US06           |
| Calculator logic       | Prompt for inputs and coordinate calculation/response                    | US01, US02           |
| User info display      | Greet user with name and ID in the terminal                              | US02                 |
| Input validation       | Prevent crashes with numeric checks and positive values only             | US03                 |

### Additional Features (Sprint 2+)

| Feature                | Description                                                                      | Linked User Stories |
|------------------------|----------------------------------------------------------------------------------|----------------------|
| File saving/loading    | Allow users to save or load loan session data (e.g. JSON or text file)           | US04, US06           |
| User authentication    | Check if user is on approved list before allowing access                         | US05                 |
| Command-based menu     | Offer choices like "Calculate again", "Exit", "View last session"                | US02, US04           |
| Automated testing      | Add unit tests for `Loan` and input validation using `unittest` or `pytest`      | US06, US07           |
| Documentation and polish | Write README, add comments, align output formatting                            | US07                 |


## Planned features by sprint

## Sprint 1 – Core Features (MVP)
- Create `User`, `Loan`, and `Calculator` classes with attributes and `__init__` methods
- Implement `User.display_info()` to show user name and ID
- Implement compound interest methods in `Loan` class: `total_due()` and `total_interest()`
- Build `Calculator.run()` method to prompt user input and display results
- Add input validation to handle incorrect types and negative values


## Sprint 2 – Functional Enhancements
- Add optional file saving/loading of loan session data (e.g. JSON or plain text)
- Extend user interface with command-based menu options: "Calculate again", "Exit", "View last session"


## Sprint 3 – Finalisation and Optional Features
- Optional: Add user authentication by verifying name and ID from a stored list
- Add automated tests for `Loan` and input functions using `unittest` or `pytest`
- Write documentation (README, inline comments, and docstrings)
- Polish command-line output formatting and user feedback messages



## Extensibility
The design supports easy addition of new features. Attributes such as `variable_or_interest`, `interest_only`, can be added to the `Loan` class. More advanced user interface options or external file formats (e.g. CSV, JSON) can be implemented with minimal disruption to the system architecture.

## Author
Rory Nathan