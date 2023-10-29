# Function to generate a Fibonacci series for a given input value 'n'
def generate_fibonacci(n):
    # If 'n' is non-positive, return an empty list as there are no Fibonacci numbers to generate
    if n <= 0:
        return []
    # If 'n' is 1, return the base case of [0]
    elif n == 1:
        return [0]
    # If 'n' is 2, return the base case of [0, 1]
    elif n == 2:
        return [0, 1]

    # Initialize the Fibonacci sequence with the base cases
    fibonacci_sequence = [0, 1]

    # Continue generating Fibonacci numbers until the sequence reaches length 'n'
    while len(fibonacci_sequence) < n:
        # Calculate the next Fibonacci number by adding the last two numbers
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    # Return the generated Fibonacci sequence
    return fibonacci_sequence

# Take user input for 'n' to generate a different number of Fibonacci sequence
n = int(input("Enter a number to generate a Fibonacci series: "))
fib_sequence = generate_fibonacci(n)

# Print the generated Fibonacci sequence
print(fib_sequence)
