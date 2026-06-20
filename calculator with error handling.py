while True:
    try:
        num1=float(input("Enter first number: "))
        num2=float(input("Enter second number: "))
    except ValueError:
        print("Invalid number!Try Again")
        continue

    operation = input("Choose operation(+,-,*,/): ")
    
    if operation == "+":
        print("Result: " +str(num1+num2))
        break
    elif operation == "-":
        print("Result: " +str(num1-num2))
        break
    elif operation == "*":
        print("Result: "+str(num1*num2))
        break
    elif operation == "/":
        try:
            print("Result: "+str(num1/num2))
            break
        except ZeroDivisionError:
            print("Cannot divide by zero!")
    else:
        print("Invalid operation! Choose +,-,* or /")       



