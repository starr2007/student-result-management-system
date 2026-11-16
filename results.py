PASS_MARK = 50

def calculate_total_and_average(scores):
    if not scores:
        return 0, 0.0
    values = [float(item["score"]) for item in scores.values()]
    total = sum(values)
    return total, total / len(values)

def assign_grade(average):
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 45:
        return "D"
    return "F"
