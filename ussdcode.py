code_dict = {"*323#": "Your data balance is: ", "*310#":"You balance is: ", "*311#": "" }
key_to_lookup = input("Enter your code: ")

if key_to_lookup == "*311#":
    input("Enter your pin: ")
    print("Recharge successful ") 
elif key_to_lookup in code_dict:
    value_at_key = code_dict[key_to_lookup]
    print(value_at_key)
else:
    print("invalid code")
