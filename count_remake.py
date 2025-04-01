# Ask the user to input a string
user_input = input("Enter a string: ")
# Ask the user what to check for its number of occurrance in the input
check_for = input("Enter a character to check for: ")
# Check if the character is in the string
if check_for in user_input:
    # If it is, print the number of times it occurs in the string
    num_of_occurance = 0
    for char in user_input:
        if char == check_for:
            num_of_occurance += 1
    print(num_of_occurance)
else:
    # If it is not, print "0"
    print(0)