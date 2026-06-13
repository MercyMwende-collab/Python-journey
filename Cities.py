Cities=("Nairobi","Mombasa","Kisumu","Nakuru","Eldoret")
for city in Cities:
    print (city)
for i in range(len(Cities)):
    print(i+1,Cities[i])

numbers=[1,2,3]
for number in numbers:
    if number %2 == 0:
        print(str(number) + " is even")
    else:
        print(str(number) + " is odd")

while True:
    name = input("Enter a name or type stop to quit: ")
    if name == "stop":
        break
    print("Hello, " + name )

Foods = ["Rice","Beans","Ugali","Chapati"]
for food in Foods:
    print(food) 
print (" I have " + str(len(Foods)) + " favourite foods")

Students = ["Caleb","Anna","Joel","Grace","Prince"]
Passed = ["Anna","Joel","Grace"]
print("Results for" + str(len(Students)) + " students")
print("_______________________")

for student in Students:
    if student in Passed:
        print(student + " -passed")
    else:
        print(student + " -failed")

print("_______________________")
print(str(len(Passed)) + " students passed out of " + str(len(Students)))

Counties = ["Makueni","Machakos","Nairobi","Turkana","Kajiado"]
With_Universities = ["Machakos","Nairobi"]

print("______________________________")
for County in Counties:
    if County in With_Universities:
        print(County + " - university")
    else:
        print(County + " - no university")

print("______________________________")
print(str(len(With_Universities)) + " counties have universities out of " + str(len(Counties)))

