print("Posible operations: Addition, Subtraction, Division, Multiplication")
val1 = input("Enter your first value")
val2 = input("Enter your second value")
operation = input("Enter your desire operation").capitalize()
if operation == "Addition":
    print(int(val1) + int(val2))
elif operation == "Subtraction":
    print(int(val1) - int(val2))
elif operation == "Division":
    print(int(val1) / int(val2))
elif operation == "Multiplication":
    print(int(val1) * int(val2))
else:
    print("invalid operation try again")
