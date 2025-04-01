# Ask the user for a string input
user_input = input("Enter a string: ")
# Use the '.upper()' method on the first character of the input
first_char_upper = user_input[0].upper()
# Use the '.lower()' method on the rest of the characters of the input
rest_chars_lower = user_input[1:].lower()
# Add these together
result = first_char_upper + rest_chars_lower
# Print the result
print(result)