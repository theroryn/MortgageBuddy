### Sprint 3 – Finalization and Optional Features

***

## Sprint goal

To finalize the **MortgageBuddy** application by implementing user authentication, storing authorized users externally, and polishing the overall user experience through improved documentation and output formatting.

***

## Tasks completed

- **User Authentication**: Implemented a basic user authentication check. The program now verifies a user's name and ID against a list of authorized users stored in an external file (`users.txt`).
- **User Experience Polish**:
  - Refined all user-facing prompts and output messages for clarity and professionalism.
  - Updated the `README.md` with detailed usage instructions, installation steps, and a system overview.
  - Added comprehensive docstrings and inline comments throughout the codebase to improve maintainability and adherence to the **SDS**.
- **Code Refinement**: Conducted a final review of the code to ensure consistency in style and formatting.
- **Manual Testing**: Performed a final round of end-to-end manual testing to confirm all features (including those from previous sprints) work as expected.

***

## Resources used

- Sprint 2 codebase: The foundation for adding new features.
- Software Design Specification (SDS): Used as the blueprint for Sprint 3 features.
- AI assistance: Utilized for best practices in improving documentation.
    - Fixing and identifying bugs in code
***

## Testing log

| Test case | Input | Expected outcome | Actual outcome | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **User Authentication - valid user** | `Name: admin`<br>`ID: 123` | Access granted, menu displayed | Confirmed | New authentication logic handled this correctly. |
| **User Authentication - invalid user** | `Name: guest`<br>`ID: 456` | Access denied, program exits | Confirmed | `main.py` successfully blocks unauthorized access. |
| **Full program run** | Valid user login, new calculation, save, view last, exit | All features function correctly in sequence | Confirmed | End-to-end flow is stable and robust. |

***

## Version control

- All changes were committed directly to the local `main` branch.
- A final push was made to the remote GitHub repository after all features were implemented and tested locally.

***

## Reflections

The implementation of user authentication with external data storage successfully meets the requirements laid out in the **SDS** and backlog. This final sprint brings the **MortgageBuddy** application to a complete and stable state, ready for potential future extensions outlined in the **SDS**. The codebase is now highly maintainable due to improved documentation and a robust, tested design.