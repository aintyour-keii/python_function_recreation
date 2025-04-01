# Define lower and upper variables containing lowercase and uppercase alphabet characters respectively
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Create a translation table which first adds the lower and upper then the upper and lower (this will be the swapping)
swap_table = str.maketrans(lower + upper, upper + lower)
# Ask the user for a string input
# Use the '.translate()' method and pass the translation table to it to swap the case of the string
user_input = input("Please enter a string: ").translate(swap_table)
# Print the input
print(user_input)