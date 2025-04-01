# Ask for the user input
user_input = input("Enter a string: ")
# Ask for the suffix to be checked
suffix_to_check = input("Enter a suffix to check: ")
# Check if the suffix is at the end of the input
endswith = user_input[-len(suffix_to_check):] == suffix_to_check
# If it is, print True. Otherwise, print False
print(endswith)