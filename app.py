def calculate_hra(basicSalary):
    hra = basicSalary * 0.2
    return hra
def calculate_da(basicSalary):
    da = basicSalary * 0.1
    return da
def calculate_net_salary(basicSalary):
    hra_value = calculate_hra(basicSalary)
    da_value = calculate_da(basicSalary)
    netSalary = basicSalary + hra_value + da_value
    return netSalary
print(calculate_net_salary(10000))

# Problem statement
def calculate_total(marks):
    return sum(marks)

def calculate_percentage(total, num_subjects):
    return total / num_subjects

def assign_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"

marks = []

for i in range(1, 6):
    mark = float(input(f"Enter marks for Subject {i}: "))
    marks.append(mark)


total = calculate_total(marks)
percentage = calculate_percentage(total, len(marks))
grade = assign_grade(percentage)

print("\n Result: ")
print("Total Marks:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade) 

# Pracitcal 1
def grade(p):
    if p >= 90:
        return "A"
    elif p >= 75:
        return "B"
    elif p >= 60:
        return "C"
    elif p >= 40:
        return "D"
    return "F"

students = {}
n = int(input("Enter number of students: "))

for i in range(n):
    roll = input("Roll No: ")
    name = input("Name: ")

    marks = []
    for j in range(5):
        marks.append(int(input(f"Subject {j+1}: ")))

    total = sum(marks)
    per = total / 5

    students[roll] = {
        "name": name,
        "marks": marks,
        "percentage": per,
        "grade": grade(per)
    }

print("\nStudent Records")
for roll, data in students.items():
    print(roll, data["name"], data["percentage"], "%", data["grade"])

topper = max(students, key=lambda x: students[x]["percentage"])

print("\nTopper:")
print(students[topper]["name"], "-", students[topper]["percentage"], "%")



