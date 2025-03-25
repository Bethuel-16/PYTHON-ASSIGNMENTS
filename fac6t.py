# Welcome the user to the program
print("Welcome to the Factorial Calculation Program!")

# Function to calculate the factorial of a number using a loop
def calculate_factorial(n):
    # Initialize the result to 1
    result = 1
    
    # Loop from 1 to n and multiply each value to result
    for i in range(1, n + 1):
        result *= i
    
    return result

# Input validation to ensure a positive integer is entered
while True:
    try:
        # Ask the user which factorial they want to calculate
        number = int(input("Enter a positive integer to calculate its factorial: "))
        
        # Check if the number is positive
        if number < 0:
            print("Please enter a positive integer.")
        else:
            # Calculate the factorial
            factorial = calculate_factorial(number)
            print(f"The factorial of {number} is {factorial}")
            break  # Exit the loop once the valid input is received
    
    except ValueError:
        # Handle non-integer inputs
        print("Invalid input. Please enter a valid positive integer.")
2
