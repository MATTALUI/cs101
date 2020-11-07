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
        return "ls
    if rem < 3:
        return "-"
    return ""

grades = []
for i in range(5):
    grades.append(float(input("What was your score? ")))
average = sum(grades) / len(grades)

letter = get_letter(average)
suffix = get_suffix(average)

print(f"For an average score of {average} your grade is a {letter}{suffix}")

# TESTS
assert get_suffix(82.9) == "-"
assert get_suffix(87) == "+"
assert get_suffix(86.9) == ""
assert get_suffix(93) == ""
assert get_suffix(92.9) == "-"
assert get_suffix(100) == ""
assert get_suffix(51) == ""
