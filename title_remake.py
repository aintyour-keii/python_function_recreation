# Ask the user to input a string
user_input = input("Enter a string: ")
# Split the string
words = user_input.split()
# Create a variable to store the modified string
modified_string = ""
# Loop throught the parts of the string
for word in words:
    # Check if the modified string is still empty, then add the first word after using the '.capitalize()' on it
    if modified_string == "":
        modified_string = word.capitalize()
    # if the modified string is not empty, Use '.capitalize()' on each part and add it onto the modified string after a space
    else:
        modified_string += " " + word.capitalize()

# After looping, print the modified string variable
print(modified_string)