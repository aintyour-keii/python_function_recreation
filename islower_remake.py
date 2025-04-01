# Ask the user to input a string
user_input = input("Enter a string: ")
# Initialize a boolean to track if the string is in all lower case
is_lower = True
# Itterate through the string
for char in user_input:
    # And check if the character is in range of "A-Z" then set the boolean to false and break
    if 'A' <= char <= 'Z':
        is_lower = False
        break

# Print the value of the boolean
print(is_lower)