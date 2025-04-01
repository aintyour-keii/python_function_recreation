# Ask the user for a string
user_string = input("Enter a string: ")
# Start from the end of the string and find the last non-space character
last_non_space_index = len(user_string) - 1
while user_string[last_non_space_index] == " ":
    last_non_space_index -= 1
# Trim the string up to the last non-space character
trimmed_string = user_string[:last_non_space_index + 1]
# Print the trimmed string
print(trimmed_string)