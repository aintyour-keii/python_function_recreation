# Ask for the user input
user_input = input("Enter a string: ")
# Ask for the prefix to be checked
prefix = input("Enter a prefix to check: ")
# Check if the prefix is at the start of the input
startswith =  user_input[:len(prefix)] == prefix
# If it is, print True. Otherwise, print False
print(startswith)