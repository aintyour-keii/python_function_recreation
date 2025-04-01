# Ask for the user input
text_input = input("Enter a string: ")
# Ask for the prefix to be removed
prefix_input = input("Enter the prefix to be removed: ")
# Check if the string starts with the prefix
if text_input[len(prefix_input):] == prefix_input:
    # If it does, remove the prefix and print the result
    print(text_input[len(prefix_input):])
else:
    # If it doesn't, print the string unmodified
    print(text_input)