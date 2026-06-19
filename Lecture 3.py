while True:
    try:
        x=int(input("What is x? "))
    except:
        print("x is not an integer")
    else:
        break
print(f"x is {x}")


try:
    x=int(input("Enter a number: "))
    result= 10/x
    print(f"Your result is :{result} ")
except ValueError:
    print("Please enter a valid number!")
except ZeroDivisionError:
    print("You cannot divide by zero!")
       
while True:
    try:
        x=int(input("Enter a number: "))
    except ValueError:
       print("Invalid! Try again")
    else:
        break
print("Valid number!")  
