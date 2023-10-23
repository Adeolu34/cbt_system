sentence = input("Enter your statement >:")
RequestToReplace = input("will you like to replace any word in the statement").capitalize()
if RequestToReplace == "Yes":
    find = input("enter the word you want to replace").capitalize()
    replace = input("enter the word you want to replace it with").capitalize()
    confirm = input("are you sure you want to replace " + find + " with " + replace + " because any correction is not revertable").capitalize()
    if confirm == "Yes":
        print(sentence.replace(find , replace))
    elif confirm == "No":
        print("Thank you, you entered "+ sentence)

else:
    print("you entered " + sentence)

