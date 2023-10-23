# import time
# # A program to calculate the grade and remark for a quiz

# StudentFirstName = input("Enter your name")
# Value1 = input("Enter your first score")
# Value2 = input("Eneter your second score")
# TotalScore = int(Value1) + int(Value2)
# print("Hi " + StudentFirstName + " your total score for this quiz is " + str(TotalScore))
# if TotalScore <= 40:
#     print("You failed the quiz")
# elif TotalScore >= 90:
#     print("You are a Star boy")
# else:
# #     print("You pass the quiz")
# import datetime

# def get_local_current_day():
#     days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#     today = datetime.datetime.now().weekday()
#     return days_of_week[today]

# if __name__ == "__main__":
#     day = get_local_current_day().capitalize()
#     print("Today is " + day)



days = ["Tuesday", "Monday" , "Wednesday" , "Thursday" , "Friday" , "Saturday" , "Sunday"]
for d in days:
    if d == "Monday":
        print(
            """ 
            Today is the first day of the week, it's time to work
            Morning: 
            Start the day with prayer and reflection.
            Attend classes and take notes actively.
            Afternoon:
            Complete any pending assignments or homework.
            Engage in extracurricular activities or clubs if you have any.
            Evening:
            Attend any study group or tutoring sessions if needed.
            Spend some time reading the Bible and meditating on its teachings.""" )
        break
    elif d == "Tuesday":
        print("""
        Never give up, for the day is brighter and you  can achieve what you set you mind to
        Morning:
        Begin with prayer and gratitude.
        Attend classes and participate in discussions.
        Afternoon:
        Focus on studying and preparing for upcoming exams.
        Take short breaks to relax and recharge.
        Evening:
        Attend any mid-week church activities or Bible study groups.
        Spend some time in personal prayer and reflection.""")
        break
    elif d == "Wednesday":
        print("""
        Hmmm, you strength is renewed wake up and tackle today man to man
        Morning:
        Start with prayer and asking for guidance for the day.
        Attend classes and actively engage with the material.
        Afternoon:
        Work on group projects or assignments with classmates.
        Take short breaks for physical activity or stretching.
        Evening:
        Attend any church-related activities or youth groups.
        Spend time in personal devotion and prayer.""")
        break
    elif d == "Thursday":
        print(
            """
            We are almost done with the week you can do it,
            Morning:
            Begin with prayer and focusing on your intentions for the day.
            Attend classes and seek clarification on any challenging topics.
            Afternoon:
            Continue studying and reviewing course materials.
            Take short breaks to go for a walk or practice mindfulness.
            Evening:
            Volunteer or participate in community service if possible.
            Spend time in personal worship and reflection.
            """
        )
        break
    elif d == "Friday":
        print(
            """
            Thank God it's friday, it is time for party
            Morning:
            Start with prayer and expressing gratitude.
            Attend classes and actively participate in discussions.
            Afternoon:
            Finish up any pending assignments or projects.
            Plan some leisure time with friends or family.
            Evening:
            Attend church service or other religious activities.
            Use this time for personal prayer and connecting with God.
            """
        )
        break
    elif d == "Saturday":
        print(
            """
            Owanbe for sure, let's get our hands dirty,
            Morning:
            Begin with prayer and asking for guidance for the day.
            Use this time to catch up on reading or self-study.
            Afternoon:
            Engage in hobbies or activities that bring you joy.
            Spend time with loved ones or friends.
            Evening:
            Attend any church-related events or gatherings.
            Reflect on the past week and set goals for the coming week.
            """
        )
        break
    elif d == "Sunday":
        print(
            """
            Remember the sabbath day to keep it holy,
            Morning:
            Start with prayer and gratitude for the new week.
            Attend Sunday church service and actively participate.
            Afternoon:
            Have a family meal and spend quality time with loved ones.
            Rest and relax, engaging in activities that rejuvenate you.
            Evening:
            Use this time for personal Bible study and reflection.
            Prepare for the week ahead, organizing your study materials.
            """
        )
        break
    else:
        print("The day you enter is wrong, check again and retry.")
        break