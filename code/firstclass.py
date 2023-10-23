# import datetime

# def get_local_current_day():
#     days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#     today = datetime.datetime.now().weekday()
#     return days_of_week[today]

# if __name__ == "__main__":
#     current_day = get_local_current_day().capitalize()

sales = input("Enter you sales for the month")
expectedSales = int(sales)
expectedSalary = 30000
if expectedSales >= 20:
    print("your salary is " + str(expectedSalary))
else:
    print("You did not make enough sale")