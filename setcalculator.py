# Get the number of sets from the user
set_input = input("Enter the number of sets: ")
num_sets = int(set_input)

# Initialize a list to store the sets
sets_list = []

# Collect sets from the user and store them in the list
for i in range(1, num_sets + 1):
    set_input = input(f"Enter set {i} elements separated by spaces: ")
    set_elements = set_input.split()
    new_set = set(set_elements)
    sets_list.append(new_set)

# Perform basic set operations
print("Possible operations: Union, Intersection, Difference")
choice = input("Enter your Operation: ").capitalize()
if choice == "Union":
    firstInput = int(input("Enter the first set to operate")) - 1
    secondInput = int(input("Enter the second set to work on")) - 1

    we = sets_list[firstInput].union(sets_list[secondInput])
    print(we)
elif choice =="Intersection":
    firstInput = int(input("Enter the first set to operate")) - 1
    secondInput = int(input("Enter the second set to work on")) - 1
    we = sets_list[firstInput].intersection(sets_list[secondInput])
    print(we)
elif choice == "Difference":
    firstInput = int(input("Enter the first set to operate")) - 1
    secondInput = int(input("Enter the second set to work on")) - 1
    we = sets_list[firstInput].difference(sets_list[secondInput])
        
