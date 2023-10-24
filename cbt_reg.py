import mysql.connector as sql

# mycon = sql.connect(host="localhost", user='root', passwd='enter your database password')
# mycursor = mycon.cursor()
# mycursor.execute("CREATE DATABASE restricted_product_db")
# def register_student():
#     # mycursor.execute("CREATE TABLE student_table (student_id INT(5), First_name VARCHAR (15), Last_name VARCHAR(15), Address VARCHAR(60), Phone VARCHAR(11), Username VARCHAR(12), Password VARCHAR(12))")
#     # Execute and consume/discard the results of the SHOW TABLES query
#     mycursor.execute("SHOW TABLES")
#     tables = mycursor.fetchall()

#     student_details = []
#     number_of_student = int(input("Enter the number of students you want to register: "))

#     for student in range(number_of_student):
#         firstname = input("Enter your first name: ")
#         lastname = input("Enter your last name: ")
#         address = input("Enter your address: ")
#         phonenumber = input("Enter your phone number: ")
#         username = input("Enter your unique username: ")
#         password = input("Enter your password: ")
#         student_turple = (firstname, lastname, address, phonenumber, username, password)
#         student_details.append(student_turple)


#     student_update = "INSERT INTO student_table (First_name, Last_name, Address, Phone, Username, Password) VALUES (%s, %s, %s, %s, %s, %s)"
#     val = student_details
#     mycursor.executemany(student_update, val)
#     mycon.commit()
#     print(mycursor.rowcount, " records inserted successfully")
#     mycon.close()
# register_student()