from results import calculate_total_and_average, assign_grade

def student_report(student):
    total, average = calculate_total_and_average(student.scores)
    lines = [
        "STUDENT REPORT CARD",
        "=" * 35,
        f"Student ID: {student.student_id}",
        f"Full Name: {student.full_name}",
        f"Class/Form: {student.class_form}",
        f"Gender: {student.gender}",
        f"Date of Birth: {student.date_of_birth}",
        "-" * 35,
        "SUBJECT SCORES"
    ]
    if student.scores:
        for subject, info in student.scores.items():
            lines.append(f"{subject}: {info['score']:.1f} (entered {info.get('date_entered', 'N/A')})")
    else:
        lines.append("No scores have been entered.")
    lines += [
        "-" * 35,
        f"Total: {total:.1f}",
        f"Average: {average:.2f}",
        f"Grade: {assign_grade(average) if student.scores else 'N/A'}",
        "=" * 35
    ]
    return "\n".join(lines)

def class_summary(students):
    students_with_scores = [s for s in students if s.scores]
    if not students_with_scores:
        return "No student results are available yet."
    averages = [calculate_total_and_average(s.scores)[1] for s in students_with_scores]
    return (
        f"Students with results: {len(students_with_scores)}\n"
        f"Highest average: {max(averages):.2f}\n"
        f"Lowest average: {min(averages):.2f}\n"
        f"Class average: {sum(averages) / len(averages):.2f}"
    )

def save_class_report(students):
    ordered = sorted(students, key=lambda s: calculate_total_and_average(s.scores)[1], reverse=True)
    lines = ["CLASS RESULT REPORT", "=" * 40]
    for student in ordered:
        total, average = calculate_total_and_average(student.scores)
        grade = assign_grade(average) if student.scores else "N/A"
        lines.append(f"{student.student_id} | {student.full_name} | Total: {total:.1f} | Average: {average:.2f} | Grade: {grade}")
    lines += ["", "CLASS STATISTICS", class_summary(students)]
    path = "class_report.txt"
    with open(path, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))
    return path
