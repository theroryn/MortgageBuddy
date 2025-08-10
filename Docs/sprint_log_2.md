# Sprint 2 – Persistence and Menu CLI

## Sprint goal

To enhance the MortgageBuddy application by adding file saving and loading of loan sessions in plain text format and implementing a menu-based command-line interface (CLI) to improve user interaction. Additional refinements were made to user prompts and output formatting.

---

## Tasks completed

- Implemented file saving of loan session data to a `.txt` file
- Implemented file loading of loan session data from a `.txt` file
- Developed a menu-based CLI with options to:
  1. Create a new loan calculation
  2. View the most recently saved loan
  3. Exit the application
- Refined program output formatting with clear headings and spacing
- Updated input prompts for clarity and precision
- Conducted manual testing to confirm functionality
- Committed changes incrementally using Git for version tracking

---

## Resources used

- Python standard library functions for file handling (`open`, `read`, `write`)
- Python standard input and output functions
- Sprint 1 class implementations carried forward as the application base
- AI assistance used for structuring the menu loop and integrating persistence logic

---

## Testing log

| Test case                  | Input                              | Expected outcome                                    | Actual outcome           | 
|----------------------------|------------------------------------|-----------------------------------------------------|--------------------------|
| New loan calculation       | Valid loan parameters              | Correct total due and interest displayed            | Success                  | 
| Save loan data (.txt)      | Save after calculation             | Loan data written to `loan_data.txt`                | Success                  | 
| Load loan data (.txt)      | Load saved loan from menu           | Loan data restored and results displayed            | Success                  | 
| Load with no file present  | Select load without save file       | Error message displayed                             | Success                  |                    |
| Load with corrupted file   | Invalid or missing values in file   | Error message displayed                             | Success                  | 
| Invalid menu selection     | Non-numeric or out-of-range input   | Error message and re-prompt                         | Success                  | 
| Exit menu                  | Select exit option                  | Program terminates                                  | Success                  | 

---

## Version control

- All Sprint 2 changes implemented on the `sprint-2` branch
- Incremental commits with descriptive messages after each functional milestone
- Added persistence methods to `Calculator.py`
- Updated `main.py` to call the new menu loop
- Branch pushed to remote repository after testing completion

---

## Reflections

The introduction of plain text persistence enables quick storage and retrieval of loan session data without external dependencies.  
The menu-based CLI allows for efficient navigation and reduces program restarts.  
Output formatting improvements increase clarity and professionalism.  
Sprint 3 will focus on user authentication, extended menu options, and automated unit testing.
