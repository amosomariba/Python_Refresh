def collatz(number):
    if number % 2 == 0:  # If the number is even
        result = number // 2
    else:  # If the number is odd
        result = 3 * number + 1
    print(result)
    return result


# Main program
try:
    user_input = int(input("Enter number: "))  # Get user input and convert to integer
    while user_input != 1:  # Continue until the sequence reaches 1
        user_input = collatz(user_input)
except ValueError:
    print("Please enter a valid integer.")
