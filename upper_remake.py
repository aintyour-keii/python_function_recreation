# Ask the user for input a string
user_input = input("Enter a string: ")
# Create a translation table for lowercase to uppercase
lower_to_upper = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
# Convert the input to uppercase using translate
uppercase_input = user_input.translate(lower_to_upper)
# Print the input
print(uppercase_input)