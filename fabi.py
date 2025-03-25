# Welcome the user to the Fibonacci Sequence program
print("Welcome to the Fibonacci Sequence Program!")

# Recursive function to calculate the nth Fibonacci number
def fibonacci(n):
    # Base cases: Fibonacci of 0 is 0, Fibonacci of 1 is 1
    if n <= 1:
        return n
    else:
        # Recursive case: Fn = Fn-1 + Fn-2
        return fibonacci(n - 1) + fibonacci(n - 2)

# Input validation to ensure a positive integer is entered
while True:
    try:
        # Ask the user how many Fibonacci terms they want to generate
        n_terms = int(input("Enter a positive integer to generate Fibonacci terms: "))
        
        # Ensure the input is a positive integer
        if n_terms <= 0:
            print("Please enter a positive integer greater than 0.")
        else:
            # Generate and print the Fibonacci sequence up to the nth term
            print(f"Fibonacci sequence up to {n_terms} terms:")
            for i in range(n_terms):
                print(fibonacci(i), end=" ")
            print()  # New line after the sequence
            break  # Exit the loop after valid input

    except ValueError:
        # Handle non-integer inputs
        print("Invalid input. Please enter a valid positive integer.")
