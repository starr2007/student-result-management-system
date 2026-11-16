from student import Student
from storage import load_students, save_students
from results import calculate_total_and_average, assign_grade
from reports import student_report, class_summary, save_class_report

def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")

def find_student(students, key):
    key = key.strip().lower()
    return next((s for s in students if s.student_id.lower() == key or s.full_name.lower() == key), None)

def add_student(students):
    student_id = get_non_empty("Student ID: ")
    if any(s.student_id.lower() == student_id.lower() for s in students):
        print("That student ID already exists.")
        return
    student = Student(
        student_id=student_id,
        full_name=get_non_empty("Full name: "),
        class_form=get_non_empty("Class/Form: "),
        gender=get_non_empty("Gender: "),
        date_of_birth=get_non_empty("Date of birth (YYYY-MM-DD): "),
        scores={}
    )
    students.append(student)
    save_students(students)
    print("Student registered successfully.")

def view_students(students):
    if not students:
        print("No students have been registered.")
        return
    print("\nREGISTERED STUDENTS")
    for s in students:
        total, average = calculate_total_and_average(s.scores)
        grade = assign_grade(average) if s.scores else "N/A"
        print(f"{s.student_id} | {s.full_name} | {s.class_form} | Total: {total:.1f} | Average: {average:.2f} | Grade: {grade}")

def search_student(students):
    student = find_student(students, input("Enter student ID or full name: "))
    print(student_report(student) if student else "Student not found.")

def update_student(students):
    student = find_student(students, input("Enter student ID or full name: "))
    if not student:
        print("Student not found.")
        return
    print("Press Enter to keep the current value.")
    for field, label in [
        ("full_name", "Full name"),
        ("class_form", "Class/Form"),
        ("gender", "Gender"),
        ("date_of_birth", "Date of birth")
    ]:
        value = input(f"{label} [{getattr(student, field)}]: ").strip()
        if value:
            setattr(student, field, value)
    save_students(students)
    print("Student information updated.")

def delete_student(students):
    student = find_student(students, input("Enter student ID or full name: "))
    if not student:
        print("Student not found.")
        return
    confirm = input(f"Delete {student.full_name}? (y/n): ").strip().lower()
    if confirm == "y":
        students.remove(student)
        save_students(students)
        print("Student record deleted.")

def record_scores(students):
    student = find_student(students, input("Enter student ID or full name: "))
    if not student:
        print("Student not found.")
        return
    print("Enter at least five subjects. Type DONE as a subject name when finished.")
    while True:
        subject = input("Subject name (or DONE): ").strip()
        if subject.lower() == "done":
            break
        if not subject:
            continue
        try:
            score = float(input(f"Score for {subject} (0-100): "))
            if not 0 <= score <= 100:
                print("Score must be between 0 and 100.")
                continue
            student.add_or_update_score(subject, score)
            save_students(students)
            print("Score saved.")
        except ValueError:
            print("Please enter a valid number.")
    if len(student.scores) < 5:
        print(f"Reminder: this student currently has {len(student.scores)} subject(s); at least five are required.")

def show_report(students):
    student = find_student(students, input("Enter student ID or full name: "))
    if not student:
        print("Student not found.")
        return
    report = student_report(student)
    print(report)
    if input("Save this report to a text file? (y/n): ").strip().lower() == "y":
        filename = f"report_{student.student_id}.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(report)
        print(f"Report saved as {filename}")

def main():
    students = load_students()
    actions = {
        "1": ("Add a student", lambda: add_student(students)),
        "2": ("View all students", lambda: view_students(students)),
        "3": ("Search for a student", lambda: search_student(students)),
        "4": ("Update student information", lambda: update_student(students)),
        "5": ("Delete a student", lambda: delete_student(students)),
        "6": ("Record or update subject scores", lambda: record_scores(students)),
        "7": ("Display a student report card", lambda: show_report(students)),
        "8": ("Show class statistics", lambda: print(class_summary(students))),
        "9": ("Sort students by average (highest first)", lambda: view_students(sorted(students, key=lambda s: calculate_total_and_average(s.scores)[1], reverse=True))),
        "10": ("Generate class report text file", lambda: print(f"Saved as {save_class_report(students)}")),
    }
    while True:
        print("\n===== STUDENT RESULT MANAGEMENT SYSTEM =====")
        for number, (label, _) in actions.items():
            print(f"{number}. {label}")
        print("0. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "0":
            save_students(students)
            print("Data saved. Goodbye!")
            break
        action = actions.get(choice)
        if action:
            try:
                action[1]()
            except (OSError, KeyError, TypeError) as error:
                print(f"Something went wrong: {error}")
        else:
            print("Invalid option. Please choose from the menu.")

if __name__ == "__main__":
    main()
