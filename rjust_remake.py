# Ask the user to input a string
user_input = input("Enter a string: ")
# Ask the user for the width
width = int(input("Enter the width of the output: "))
# Check if string needs extra spaces
if len(user_input) < width:
    # If so, add spaces before the string, 
    # the number of spaces is equal to that of the width minus the length of the string
    user_input = " " * (width - len(user_input)) + user_input

# Print the result
print(user_input)