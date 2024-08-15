# Get a numeric grade (0-100) from the user
numeric_grade = int(input("Enter the numeric grade (0-100): "))

# User selects the grading scheme
grading_scheme = input("Enter 'SG' for Standard Grading or 'PMG' for Plus-Minus Grading: ").upper()

# Determine the grade based on the selected scheme
if grading_scheme == 'SG':
    # Standard Grading Scheme
    if 100 >= numeric_grade >= 90:
        grade = 'A'
    else:
        if numeric_grade >= 80:
            grade = 'B'
        else:
            if numeric_grade >= 70:
                grade = 'C'
            else:
                if numeric_grade >= 60:
                    grade = 'D'
                else:
                    grade = 'F'
else:
    # Plus-Minus Grading Scheme
    if numeric_grade >= 97:
        grade = 'A+'
    else:
        if numeric_grade >= 93:
            grade = 'A'
        else:
            if numeric_grade >= 90:
                grade = 'A-'
            else:
                if numeric_grade >= 87:
                    grade = 'B+'
                else:
                    if numeric_grade >= 83:
                        grade = 'B'
                    else:
                        if numeric_grade >= 80:
                            grade = 'B-'
                        else:
                            if numeric_grade >= 77:
                                grade = 'C+'
                            else:
                                if numeric_grade >= 73:
                                    grade = 'C'
                                else:
                                    if numeric_grade >= 70:
                                        grade = 'C-'
                                    else:
                                        if numeric_grade >= 67:
                                            grade = 'D+'
                                        else:
                                            if numeric_grade >= 63:
                                                grade = 'D'
                                            else:
                                                if numeric_grade >= 60:
                                                    grade = 'D-'
                                                else:
                                                    grade = 'F'


# Output the result
if grade != "Invalid grading scheme":
    print(f"The corresponding letter grade is {grade}.")
else:
    print(grade)
