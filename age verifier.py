while True:
    try:
        age=int(input("What's your age? "))
    except ValueError:
        print ("numbers only please!")
    else:
        if 1 <= age <= 120:
            print(f"Welcome your age is {age} years old")
            break
        else:
            print("Enter a realistic age")
            