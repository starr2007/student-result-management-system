import json
from pathlib import Path
from student import Student

DATA_FILE = Path(__file__).parent / "data" / "students.json"

def load_students():
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            raw_data = json.load(file)
        return [Student.from_dict(item) for item in raw_data]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Warning: the data file is empty or damaged. Starting with no records.")
        return []

def save_students(students):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump([student.to_dict() for student in students], file, indent=4)
