import csv

results = []

for i in range(4):
    name = input("Enter your name: ")
    grade = input("Enter your grade: ")
    results.append([name , grade])

with open("results.csv" , "w" , newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Grade"])
    writer.writerows(results)

print("Results Saved!")

total=0
grades=[]

with open("results.csv" , "r") as file:
    reader = csv.reader(file)
    next(reader)
    print("\n--- Class results ---")

    for row in reader:
        print(row[0] + " - Grade: " + row[1])
        grades.append(float(row[1]))
        total += float(row[1])

average = total / len(grades)
print("\nClass Average: " + str(average))

highest = max(grades)
for row in grades:
    if row == highest:
        print("Highest score: " + str(highest))