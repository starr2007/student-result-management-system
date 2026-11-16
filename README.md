# Student Result Management System

## Project description
A menu-driven Python application for registering students, recording subject scores, calculating totals and averages, assigning grades, and producing student and class reports.

## Requirements
- Python 3.9 or later
- No external packages are required.

## How to run
1. Download or clone this project.
2. Open the `student_result_system` folder in VS Code.
3. Open the terminal in that folder.
4. Run:

   `python3 main.py`

## Project files
- `main.py`: displays the menu and controls the application.
- `student.py`: defines the Student class and score-entry method.
- `results.py`: calculates totals, averages, and grades.
- `storage.py`: loads and saves records in JSON format.
- `reports.py`: creates report cards and class reports.
- `data/students.json`: stores student records.

## Grade scale used
- A: 70–100
- B: 60–69.99
- C: 50–59.99
- D: 45–49.99
- F: below 45

## Notes
The program starts with an empty student list if the JSON data file does not exist. Records are saved automatically when changes are made. Scores are expected to be between 0 and 100.

Before presenting this project, test each menu option, personalise the project to your class requirements, and make sure you can explain the functions, Student class, JSON file handling, sorting, and exception handling.
