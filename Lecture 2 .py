i=1
while i<=10:
    print(i)
    i+=1

for i in range(1 ,6):
    print(i * 2)

languages=["Python","Java","R","SQL"]
for language in languages:
    print("I am learning" + language)
print("Total languages" + str(len(languages)))

banks={"KCB", "Equity_Bank", "Absa", "Cooperative_Bank", "NCBA"}
for number, bank in enumerate(banks, 1):
    print(str(number) +"" + bank)

for i in range(10,0,-1):
    print(i)
print("Blast Off!")

numbers = { 10,20,30,40,50}
total = 0
for number in numbers:
    total=total+number

print("Total is " + str(total))

while True:
    password = input("Enter password: ")
    if password =="1234":
        print("Access granted!")
        break

    else:
        print("Wrong password, try again!")

subjects=["Mathematics","Data Science","Statistics","Programming","Data Base"]
grade=["A","B","A","C","B"]
for number, subjects in enumerate (subjects , 1):
    print(str(number) + ". " + subjects + "-" + grade[number-1])