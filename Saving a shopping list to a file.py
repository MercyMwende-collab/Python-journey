import csv

items=[]

for i in range(3):
    item = input("Enter item: ")
    items.append([item])

with open("shopping.csv", "w" ,newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Item"])
    writer.writerows(items)

print("Shopping list saved!")

with open("shopping.csv", "r") as file:
    reader = csv.reader(file)

    print("\n--- Your Shopping List ---")

    next(reader)

    for row in reader:
        print("- " + row[0])








            