import datetime

def get_local_current_day():
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    today = datetime.datetime.now().weekday()
    return days_of_week[today]

current_time = int(datetime.datetime.now().strftime("%H"))

def schedule_monday(current_time):
    if current_time < 12:
        print("""
        Start the day with prayer and reflection.
        Attend classes and take notes actively.
        """)
    elif current_time < 18:
        print("""
        Complete any pending assignments or homework.
        Engage in extracurricular activities or clubs if you have any.
        """)
    else:
        print("""
        Attend any study group or tutoring sessions if needed.
        Spend some time reading the Bible and meditating on its teachings.
        """)
def schedule_tuesday(current_time):
    if current_time >= 00:
            print("""
              Begin with prayer and gratitude.
                Attend classes and participate in discussions.
              """)
    elif current_time >= 12:
            print("""
              Focus on studying and preparing for upcoming exams.
                Take short breaks to relax and recharge.
              """)
    elif current_time >= 18:
            print("""
                Attend any mid-week church activities or Bible study groups.
                Spend some time in personal prayer and reflection.
              """)
def schedule_wednesday(current_time):
    if current_time >= 00:
            print("""
              Start with prayer and asking for guidance for the day.
                Attend classes and actively engage with the material.
              """)
    elif current_time >= 12:
            print("""
              Work on group projects or assignments with classmates.
                Take short breaks for physical activity or stretching.
              """)
    elif current_time >= 18:
            print("""
                Attend any church-related activities or youth groups.
                Spend time in personal devotion and prayer.
              """)
def schedule_thursday(current_time):
    if current_time >= 00:
            print("""
              Begin with prayer and focusing on your intentions for the day.
                Attend classes and seek clarification on any challenging topics.
              """)
    elif current_time >= 12:
            print("""
              Continue studying and reviewing course materials.
                Take short breaks to go for a walk or practice mindfulness.
              """)
    elif current_time >= 18:
            print("""
                Volunteer or participate in community service if possible.
                Spend time in personal worship and reflection.
              """)
def schedule_friday(current_time):
    if current_time >= 00 and current_time < 12:
            print("""
              Start with prayer and expressing gratitude.
                Attend classes and actively participate in discussions.
              """)
    elif current_time >= 12 and current_time < 18:
            print("""
              Finish up any pending assignments or projects.
                Plan some leisure time with friends or family.
              """)
    elif current_time >= 18:
            print("""
                Attend church service or other religious activities.
                Use this time for personal prayer and connecting with God.
              """)
def schedule_saturday(current_time):
    if current_time >= 00 and current_time < 12:
            print("""
              Begin with prayer and asking for guidance for the day.
                Use this time to catch up on reading or self-study.
              """)
    elif current_time >= 12 and current_time < 18:
            print("""
              Finish up any pending assignments or projects.
                Plan some leisure time with friends or family.
              """)
    elif current_time >= 18:
            print("""
                Attend any church-related events or gatherings.
                Reflect on the past week and set goals for the coming week.
              """)
def schedule_sunday(current_time):
    if current_time >= 00 and current_time < 12:
            print("""
              Start with prayer and gratitude for the new week.
                Attend Sunday church service and actively participate.
              """)
    elif current_time >= 12 and current_time < 18:
            print("""
              Have a family meal and spend quality time with loved ones.
                Rest and relax, engaging in activities that rejuvenate you.
              """)
    elif current_time >= 18:
            print("""
                Use this time for personal Bible study and reflection.
                Prepare for the week ahead, organizing your study materials.
              """)
days = ["Tuesday", "Monday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for day in days:
    if day == get_local_current_day():
        if day == "Monday":
            schedule_monday(current_time)
        elif day == "Tuesday":
            schedule_tuesday(current_time)
        elif day == "Wednesday":
            schedule_wednesday(current_time)
        elif day == "Thursday":
            schedule_thursday(current_time)
        elif day == "Friday":
            schedule_friday(current_time)
        elif day == "Saturday":
            schedule_saturday(current_time)
        elif day == "Sunday":
            schedule_sunday(current_time)
if __name__ == "__main__":
    day = get_local_current_day().capitalize()
    print(f"Today is {day}")
