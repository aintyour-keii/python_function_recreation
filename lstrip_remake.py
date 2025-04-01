# Ask for user input
user_input = input("Enter a string with leading spaces: ")
# Find the first non-space character in the input
non_space_index = 0
while non_space_index < len(user_input) and user_input[non_space_index] == " ":
    non_space_index += 1
# Trim the input from the first non-space character
trimmed_input = user_input[non_space_index:]
# Print the modified input
print(trimmed_input)