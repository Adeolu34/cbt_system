num = int(input("Enter the desired number: "))
checker = num%2
if checker == 0:
    print(str(num) + " is an even number")
elif checker > 0:
    print(str(num) + " is a odd number")
else:
    print("Enter a valid number")



year = int(input("Enter the year you want to check: "))
if year%4 == 0 and year%2 == 0 and year%400 == 0:
    print(str(year) + " is a leap year")
else:
    print("is not a leap year")