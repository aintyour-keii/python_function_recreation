# Ask for the user input
user_input = input("Enter a string: ")
# Ask for the substring to find
substring = input("Enter a substring to find: ")
# Initialize a variable to store the index
index = -1
# Loop through the input in reverse
for i in range(len(user_input) - len(substring), -1, -1):
    # If the substring was found, print its index
    if user_input[i:i+len(substring)] == substring:
        index = i
        break

# If the substring was found, print its index
if index >= 0:
    print(f"The substring '{substring}' was found at index: {index}.")
else:
    print(f"The substring '{substring}' was not found in the string.")