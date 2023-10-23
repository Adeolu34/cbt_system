questions = [
    "State Newton's Second Law of Motion",
    "What is the Law of Conservation of Energy?",
    "Explain Hooke's Law in relation to springs.",
    "What is the theory of Special Relativity proposed by Albert Einstein?",
    "Explain the concept of gravitational potential energy."
]

answers = [
    ["newton's" ,"second" ,"law", "motion", "acceleration", "object", "net", "force", "mass"],
    ["law of conservation of energy", "energy", "isolated system", "change forms", "closed system"],
    ["Hooke's Law", "springs", "force", "deformation", "displacement", "proportional"],
    ["Special Relativity", "Albert Einstein", "theory", "space", "time", "constant velocity", "laws of physics", "observers", "speed of light", "relative motion", "mass", "energy", "equation E=mc²"],
    ["gravitational potential energy", "energy", "object", "position", "gravitational field", "mass", "acceleration due to gravity", "height", "reference point", "formula PE = mgh"]
]

increase = "You are right"
score = 0

for question_num, question in enumerate(questions):
    print(question)
    user_answer = input("Enter your answer > ").lower()
    user_keywords = user_answer.split()  # Split user's answer into keywords
    
    matching_keywords = set(user_keywords) & set(answers[question_num])  # Find matching keywords
    print(matching_keywords)    
    if matching_keywords and len(matching_keywords) >= ((len(answers[question_num])/2) +2):

        print(increase)
        score += 5
    else:
        print("You are wrong")
print(str(score) +"/" + str((question_num + 1)*5))
