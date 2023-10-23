import random
happy = [ "I am overflowing with joy and positivity.", "Every day brings new reasons for me to be grateful and happy.", "Happiness radiates from within me, touching everything around me.", "I deserve all the happiness that comes my way.", "I am the creator of my own happiness, and I choose to create a joyful life.", "I attract positivity and happiness into my life effortlessly.", "My heart is full of happiness, and I share it with the world.", "I find joy in the simple pleasures of life.", "Happiness is my natural state of being, and I embrace it fully.", "I am a magnet for happiness and it flows to me abundantly."
]
sad = ["I am strong, and I will overcome this challenging time.", "I am worthy of love, support, and healing.", "I embrace my emotions and allow myself to heal with time.", "I am not defined by my struggles; I am defined by my strength in overcoming them.", "I have the power to transform my pain into growth and wisdom.", "I am resilient, and I will rise above this darkness.", "Every day is a step forward on my journey to healing and happiness." , "I am surrounded by love and support, even during difficult times." , "I am capable of finding light even in the midst of darkness." , "I am on a path of healing and self-discovery, and I am making progress."]
motivation = ["I am fully capable of achieving my goals and dreams.", "I am motivated, focused, and ready to take on any challenge." , "I am in control of my actions, and I choose to take productive steps forward." , "I believe in my abilities and trust the journey I'm on." , "Obstacles are opportunities in disguise, and I embrace them to grow stronger." , "I am committed to my goals, and I will persist until I succeed." , "I am the driver of my own success, and I steer myself towards greatness." , "I am constantly evolving and improving, inching closer to my aspirations." , "I am energized by my dreams, and that energy fuels my determination." , "I am unstoppable, and nothing can stand in the way of my determination and drive."]
mood = int(input("press 1 if you are happy, press 2 if you are sad and press 3 if you need motivation: "))
if mood == 1:
    random_item = random.choice(happy)
    print(random_item)
elif mood == 2:
    random_item = random.choice(sad)
    print(random_item)
elif mood == 3:
    random_item = random.choice(motivation)
    print(random_item)
else:
    print("Invalid entry")