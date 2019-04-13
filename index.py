first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
operation = input("Enter operation [+, -, *, /]: ")

if operation == "+":
    print(first_number + second_number)
if operation == "-":
    print(first_number - second_number)
if operation == "*":
    print(first_number * second_number)
if operation == "/":
    print(first_number / second_number)
else:
    print("Error - Your request cannot be completed")