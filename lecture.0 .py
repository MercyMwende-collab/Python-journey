# < less than
# > greater than
# <= less than or equal to
# >= greater than or equal to
# == equal to
# != not equal to

x = int(input("What's x? "))
y = int(input("What's y? "))
if x>y:
    print ("x is greater than y")

elif x<y:
    print ("x is less than y")  

else:
    print ("x is equal to y")   

if x>y or x<y:
    print ("x is not equal to y")   
else:
    print ("x is equal to y")
# if
# elif
# else
# or
# and

score = int(input("Score: "))
if score >= 90:
    print ("Grade: A")
elif score >= 80:
    print ("Grade: B")
elif score >= 70:   
    print ("Grade: C")      
elif score >= 60:
    print ("Grade: D")  
else:
    print ("Grade: F")   


x =int(input("What's x? "))
if x%2 == 0:
    print ("Even")
else:
    print ("Odd")   

name = input("What's your name? ")
age = int(input("How old are you? "))
if age>= 18:
    print ("Welcome, " + name + "! You are old enough to vote.")
elif age <= 18 and age >= 13:
    print ("Hi, " + name + "! You are a teenager.")
else:
    print ("Hey, " + name + "! You are a young.")

number = int(input("Insert a number: "))
if number >= 1:
    print ("This number is positive")
elif number <= -1:
    print ("This number is negative")
elif number ==0:
    print ("This number is zero")
    
