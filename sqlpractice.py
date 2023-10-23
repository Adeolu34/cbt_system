import mysql.connector as sql
import re  # Import the regular expressions module

def connect_to_database():
    mycon = sql.connect(host="localhost", user='root', passwd='Ade@2018', database="reg_db")
    mycursor = mycon.cursor()
    return mycon, mycursor

def create_result_table():
    mycon, mycursor = connect_to_database()
    if mycon and mycursor:
        mycursor.execute("CREATE TABLE IF NOT EXISTS result_table (student_id INT(5), student_name VARCHAR(30), subject VARCHAR(25), score INT(3))")
        mycon.commit()
        mycon.close()
    else:
        print("Database connection failed.")

def is_valid_phone_number(phone_number):
    # Use regular expressions to validate the phone number
    # Here's a simple example that checks for a 10-digit number
    pattern = r"^\d{10}$"
    return re.match(pattern, phone_number)

def register_student():
    mycon, mycursor = connect_to_database()
    if mycon and mycursor:
        mycursor.execute("SHOW TABLES")
        tables = mycursor.fetchall()

        student_details = []
        number_of_student = int(input("Enter the number of students you want to register: "))

        for student in range(number_of_student):
            firstname = input("Enter your first name: ")
            lastname = input("Enter your last name: ")
            address = input("Enter your address: ")
            phonenumber = input("Enter your phone number: ")

            # Validate the phone number
            if not is_valid_phone_number(phonenumber):
                print("Invalid phone number format. Please enter a 11-digit number.")
                continue  # Skip this student's registration

            username = input("Enter your unique username: ")
            password = input("Enter your password: ")
            student_turple = (firstname, lastname, address, phonenumber, username, password)
            student_details.append(student_turple)

        student_update = "INSERT INTO student_table (First_name, Last_name, Address, Phone, Username, Password) VALUES (%s, %s, %s, %s, %s, %s)"
        val = student_details
        mycursor.executemany(student_update, val)
        mycon.commit()
        print(mycursor.rowcount, " records inserted successfully")
        mycon.close()
    else:
        print("Database connection failed.")

def question_upload():
    mycon, mycursor = connect_to_database()
    if mycon and mycursor:
        question_details = []
        question_num = int(input("Enter the number of questions to set: "))
        for question in range(question_num):
            Subject = input("Enter the subject: ")[:25]  # Limit subject to 25 characters
            Question = input("Enter question: ")
            option_a = input("Enter the first option: ")
            option_b = input("Enter the second option: ")
            option_c = input("Enter the third option: ")
            option_d = input("Enter the fourth option: ")
            correct_option = input("Enter the correct option: ")

            question_turple = (Subject, Question, option_a, option_b, option_c, option_d, correct_option)
            question_details.append(question_turple)

        question_update = "INSERT INTO cbt (Subject, question_text, option_a, option_b, option_c, option_d, correct_answer) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = question_details
        mycursor.executemany(question_update, val)
        mycon.commit()
        print(mycursor.rowcount, " records inserted successfully")
        mycon.close()
    else:
        print("Database connection failed.")

def login(mycursor):
    while True:
        user = input("Enter your username: ")
        password = input("Enter your password: ")
        query = "SELECT Username, Password FROM student_table WHERE Username = %s AND Password = %s"
        val = (user, password)
        mycursor.execute(query, val)
        validate = mycursor.fetchone()

        if validate:
            print(f"Welcome {validate[0]}")
            return validate[0]  # Return the student's username
        else:
            print("Invalid login, try again")

def record_test_result(student_username, subject, score):
    mycon, mycursor = connect_to_database()
    if mycon and mycursor:
        # Fetch the student_id based on the username
        query = "SELECT student_id FROM student_table WHERE Username = %s"
        mycursor.execute(query, (student_username,))
        student_id = mycursor.fetchone()[0]

        # Insert the test result into the result_table
        insert_query = "INSERT INTO result_table (student_id, student_name, subject, score) VALUES (%s, %s, %s, %s)"
        student_name = student_username  # You can adjust this to fetch the actual student name
        result_data = (student_id, student_name, subject, score)
        mycursor.execute(insert_query, result_data)
        mycon.commit()
        mycon.close()
    else:
        print("Database connection failed.")

def retrieve_and_print_questions(mycursor):
    mycursor.execute("SELECT DISTINCT Subject FROM cbt")
    subjects = [subject[0] for subject in mycursor.fetchall()]

    print("Available Subjects:")
    for i, subject in enumerate(subjects, start=1):
        print(f"{i}. {subject}")

    subject_choice = input("Enter the number of the subject you want to take: ")

    if subject_choice.isdigit() and 1 <= int(subject_choice) <= len(subjects):
        selected_subject = subjects[int(subject_choice) - 1]

        mycursor.execute("SELECT question_text, option_a, option_b, option_c, option_d, correct_answer FROM cbt WHERE Subject = %s", (selected_subject,))
        questions = mycursor.fetchall()

        score = 0
        for question_num, question in enumerate(questions):
            print(f"Question {question_num + 1}: {question[0]}")
            print("Options:")
            print("A. " + question[1])
            print("B. " + question[2])
            print("C. " + question[3])
            print("D. " + question[4])
            print()
            answer = input("Enter your answer: ").capitalize()
            if answer == question[5].capitalize():
                print("You are correct")
                score += 2
            else:
                print("You are wrong")

        print(f"Your score is {score}")
        return score
    else:
        print("Invalid subject choice. Please enter a valid subject number.")

def view_results():
    mycon, mycursor = connect_to_database()
    if mycon and mycursor:
        student_username = input("Enter your username to view results: ")
        query = "SELECT student_id, subject, score FROM result_table WHERE student_name = %s"
        mycursor.execute(query, (student_username,))
        results = mycursor.fetchall()

        if results:
            print(f"Results for {student_username}:")
            total_score = 0  # Initialize the total score
            for result in results:
                print(f"Subject: {result[1]}, Score: {result[2]}")
                total_score += result[2]  # Update the total score
            print(f"Total Score: {total_score}")  # Display the total score
            return total_score  # Return the total score
        else:
            print("No results found for this username.")
        mycon.close()
    else:
        print("Database connection failed.")

def main():
    create_result_table()
    
    while True:
        operations = int(input('''Press 1 to register students
Press 2 to set new questions
Press 3 to take a test
Press 4 to view results
Press 5 to exit: '''))

        if operations == 1:
            register_student()
        elif operations == 2:
            question_upload()
        elif operations == 3:
            mycon, mycursor = connect_to_database()
            if mycon and mycursor:
                student_username = login(mycursor)
                if student_username:
                    score = retrieve_and_print_questions(mycursor)  # Get the score
                    # Add code here to record the test result
                    subject = input("Enter the subject you took the test for: ")[:25]  # Limit subject to 25 characters                    
                    record_test_result(student_username, subject, score)  # Update the score
                mycon.close()
            else:
                print("Database connection failed.")
        elif operations == 4:
            total_score = view_results()  # Get the total score
            if total_score is not None:
                # Update the score in the result table
                student_username = input("Enter your username to update the score: ")
                record_test_result(student_username, "", total_score)  # Update the score
                print("Score updated successfully.")
        elif operations == 5:
            break
        else:
            print("Invalid entry, try again")

if __name__ == "__main__":
    main()
