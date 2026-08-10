# Student Grade Calculator

def calculate_grade(average_marks):
    if average_marks >= 90:
        return "O"
    elif average_marks >= 75:
        return "A+"
    elif average_marks >= 60:
        return "A"
    elif average_marks >= 55:
        return "B+"
    elif average_marks >= 50:
        return "B"
    elif average_marks >= 45:
        return "C"
    elif average_marks >= 40:
        return "D"
    else:
        return "F"

# Get student information
student_name=input("Enter student name:  ")
number_of_subjects = int(input("Enter number of subjects: "))

print("student: ", student_name)
print("Number of subjects: ", number_of_subjects)

#Get marks for each subject
marks = []

for i in range(number_of_subjects):
    while True:
        mark = float(input(f"Enter marks for subject {i + 1}: "))

        if 0 <= mark <= 100:
            marks.append(mark)
            break
        else:
            print("Please enter marks between 0 and 100.")

print("Marks: ", marks)

#Calculate total and average marks
total_marks = sum(marks)
average_marks = total_marks/ number_of_subjects

print("Total marks:  ", total_marks )
print(" Average marks : ", average_marks)

#Determine grade
grade = calculate_grade(average_marks)

# Determine pass or fail
if average_marks >= 40:
    result = "Pass"
else:
    result = "Promoted"

#Display final result
print ("\n----Student Result----")
print("Name: ", student_name)
print("Total Marks: ", total_marks)
print("Average: ", average_marks)
print("Grade: ", grade)
print("Result: ", result)
print("--------------------------")