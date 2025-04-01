# Ask the user for an input
user_input = input("Please enter a string: ")
# Ask the user for the number of characters
num_chars = int(input("Please enter the number of characters: "))
# Check if the length of the input is less than that to the number of characters
if len(user_input) < num_chars: # If it is:
    # Compute the number of zeros to be added to the input
    num_of_zeros = num_chars - len(user_input)
    # Add the zeros at the beginning of the input
    user_input = '0' * num_of_zeros + user_input

# Print the result
print(user_input)