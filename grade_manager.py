students = []

for i in range(3):
    name = (input("Enter student name: "))
    grade = int(input("Enter grade: "))
    students.append(f"{name} , {grade}")
    print(name,grade)

    with open("grades.txt", "w") as file:
        for student in students:
            file.write(student + "\n")

print("Data saved successfully!")
  
print("/n ---Students_Results---" )

with open ("grades.txt","r") as file:
    lines=file.readlines()

lines.sort()

for line in lines:
    name, grade = line.strip().split(",")
    grade = int(grade)
    if grade >= 50:
        status = "Passed"
    else:
        status = "failed"
    print(f"{name}-{grade}-{status}")


