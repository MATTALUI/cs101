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


grade = float(input("What was your score? "))
letter = get_letter(grade)
suffix = get_suffix(grade)

print(f"For a score of {grade} your grde is a {letter}{suffix}")

# TESTS
assert get_suffix(82.9) == "-"
assert get_suffix(87) == "+"
assert get_suffix(86.9) == ""
assert get_suffix(93) == ""
assert get_suffix(92.9) == "-"
assert get_suffix(100) == ""
assert get_suffix(51) == ""
