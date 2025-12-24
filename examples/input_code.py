# Example 1: Simple function
def is_even(number):
    return number % 2 == 0


# Example 2: Slightly more complex function
def calculate_average(numbers):
    if not numbers:
        return 0

    total = 0
    for value in numbers:
        total += value

    return total / len(numbers)


# Example 3: Code with a syntax error (for error handling demonstration)
def broken_function(x, y)
    return x + y
