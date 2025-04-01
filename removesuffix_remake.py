# Ask for the user input
user_input = input("Enter a string: ")
# Ask for the suffix to be removed
suffix_to_remove = input("Enter the suffix to be removed: ")
# Check if the string ends with the suffix
if user_input[-len(suffix_to_remove):] == suffix_to_remove:
    # If it does, remove the suffix and print the result
    print(user_input[:-len(suffix_to_remove)])
else:
    # If it doesn't, print the string unmodified
    print(user_input)