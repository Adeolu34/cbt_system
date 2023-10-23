Questions = [
    "Question 1: What is the primary function of the mitochondria in a eukaryotic cell? \n A) Protein synthesis \n B) Lipid storage \n C) Energy production \n D) Cell division",
    "Question 2: Which of the following is a characteristic of a prokaryotic cell?\n A) Membrane-bound nucleus \n B) Presence of mitochondria \n C) Complex organelles \n D) Lack of membrane-bound organelles",
    "Question 3: Which of the following is responsible for carrying oxygen in the blood?\n A) Platelets\n B) White blood cells\n C) Red blood cells\n D) Plasma",
    "Question 4: What is the process by which plants convert light energy into chemical energy stored in glucose? \n A) Osmosis \n B) Fermentation \n C) Photosynthesis \n D) Respiration",
    "Question 5: Which molecule stores genetic information in cells? \n A) Ribosome \n B) Lipid \n C) DNA \n D) Enzyme",
    "Question 6: What is the smallest unit of life that can carry out all the processes necessary for life? \n A) Cell \n B) Organelle \n C) Molecule \n D) Atom",
    "Question 7: Which of the following is responsible for breaking down cellular waste and cellular debris? \n A) Nucleus \n B) Lysosome \n C) Golgi apparatus \n D) Endoplasmic reticulum",
    "Question 8: Which process involves the movement of molecules from an area of high concentration to an area of low concentration, without the use of energy? \n A) Active transport \n B) Osmosis \n C) Diffusion \n D) Endocytosis",
    "Question 9: What is the role of the pancreas in the digestive system? \n A) Production of bile \n B) Storage of nutrients \n C) Regulation of blood sugar levels \n D) Absorption of nutrients",
    "Question 10: What is the function of the ribosomes in a cell? \n A) Cellular respiration \n B) Protein synthesis \n C) Lipid synthesis \nD) DNA replication"
]

Answer = ["C", "D", "C", "C", "C", "A", "B", "C", "C", "B"]

rangeSet = int(input("Enter the number of applicants > "))
student_record = {}
highest_score = 0
score_list = []
top_student = None

for i in range(1, rangeSet + 1):
    print("Enter the information for student", i)
    name = input("Enter your full name > ").capitalize()
    level = input("Enter your level > ").capitalize()
    location = input("Enter your current location > ").capitalize()
    dept = input("Enter your current department > ").capitalize()
    score = 0    
    student = {"name": name, "level": level,
               "location": location, "dept": dept, "score": score}
    student_record[name] = student
for student in student_record:
    print(student + " please take your test")
    for question_num, que in enumerate(Questions):
        print(que)
        ans = input("Pick your option > ").capitalize()

        if ans == Answer[question_num]:
            print("You are correct")
            score += 2
        else:
            print("You are wrong")
    student_record[student]["score"] = score
    score_list.append(score) 

    total_score = 2 * len(Questions)  # Total possible score
    print("Your total score is: " + str(score) + "/" + str(total_score))
print("Student with the highest score")
for studentName in student_record.values():
    if studentName["score"] == max(score_list):
        print("Congratulations ", studentName["name"] + ", having gotten the score of  " + str(studentName["score"]) + " you have won the competition")
