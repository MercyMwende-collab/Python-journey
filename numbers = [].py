numbers = []

for i in range(5):
    try:
        num = float(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        print("Invalid! Skipping...")

print("Valid numbers: " + str(numbers))
print("Total: " + str(sum(numbers)))
print("Average: " + str(sum(numbers) / len(numbers)))