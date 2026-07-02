import csv

counties=[]

for i in range(5):
    county = input("Enter a county: ")
    counties.append([county])

with open ("counties.csv", "w" , newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["County"])
    writer.writerows(counties)

print("Counties saved!")
with open ("counties.csv", "r") as file:
   reader = csv.reader(file)

   print("\n--- Kenyan counties ---")

   next(reader)

   for (row) in reader:
       print("- " + row[0])

   

