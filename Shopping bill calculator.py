Items=["Milk","Bread","Sugar","Rice","Salt"]
Price=[60,65,130,350,30]
for number , item in enumerate ( Items, 1):
    print(str(number) + "." + item + "-" + "KES" + str(Price[number-1]))

total=sum(Price)
print("Total Bill is KES "+ str(total))
