# Assignment 1
#Question 1
file = open("marks.txt","w+")
file.write("Rohan : 25 \nRahul : 67 \nRam : 44 \nKaran : 93 \nBhanghu : 88")
file.close()

file = open("marks.txt","r")
cont = file.read()
print(cont)
file.close()


file = open("marks.txt", "r")

pass_count = 0
fail_count = 0

for i in file:
    name, marks = i.split(":")
    marks = int(marks.strip())
    name = name.strip()

    if marks > 45:
        print(name, "has passed the exam with", marks, "marks")
        pass_count += 1
    else:
        print(name, "has failed the exam with", marks, "marks")
        fail_count += 1

file.close()

print("\nPass Students:", pass_count)
print("Fail Students:", fail_count)

#Question 2
file = open("salary.txt","w+")
file.write("Rohan : 25000 \nRahul : 67000 \nRam : 44000 \nKaran : 93000 \nBhanghu : 88000")
file.close()

file = open("salary.txt","r")
cont = file.read()
print(cont)
file.close()

file = open("salary.txt", "r")

employee_count=0

for i in file:
    name, salary = i.split(":")
    salary = int(salary.strip())
    name = name.strip()

    if salary > 50000:
        print(name, "has salary greater than 50k")
        employee_count += 1
    else:
        print(name, "has salary less than 50k")


file.close()

print("\nEmployee count with salary greater than 50k:", employee_count)

#Question 3
file = open("attendance.txt","w+")
file.write("Rohan : Absent \nRahul : Present \nRam : Present \nKaran : Present \nBhanghu : Absent")
file.close()

file = open("attendance.txt","r")
cont = file.read()
print(cont)
file.close()
file = open("attendance.txt", "r")

abs_count = 0
pre_count = 0

for i in file:
    name, attendance = i.split(":")
    attendance = attendance.strip()
    name = name.strip()

    if attendance == "Present":
        pre_count += 1
    else:
        print(name, "is absent")
        abs_count += 1

file.close()
total_students = pre_count + abs_count
print("\nTotal Students:", total_students)
