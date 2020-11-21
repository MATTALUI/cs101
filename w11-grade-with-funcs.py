def get_letter(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    return "F"

def get_suffix(grade):
    rem = grade % 10
    if grade > 93 or grade < 60 or rem == 0:
        return ""
    if rem >= 7:
        return "+"
    if rem < 3:
        return "-"
    return ""

def main():
    classes = ["Math", "English", "PE", "Science", "Art"]
    grades = []
    for class_name in classes:
        grades.append(float(input(f"What was your score in {class_name}? ")))
    print()
    for i in range(len(grades)):
        class_name = classes[i]
        grade = grades[i]
        letter = get_letter(grade)
        suffix = get_suffix(grade)
        print(f"Your {class_name} score was {grade}, you got {letter}{suffix}")

if __name__ == "__main__":
    main()

# TESTS
assert get_suffix(82.9) == "-"
assert get_suffix(87) == "+"
assert get_suffix(86.9) == ""
assert get_suffix(93) == ""
assert get_suffix(92.9) == "-"
assert get_suffix(100) == ""
assert get_suffix(51) == ""
