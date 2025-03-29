#
# At the second congress of the Bajtocki Informatics Society, the participants are seated around a circular table.
# One participant posed the question: how many ways can they greet each other without standing up?
# A greeting consists of each participant shaking hands with at most one of their neighbors.
# The number of ways can be large, so they are only interested in the last digit of the result.

# Input:
# n: Number of people in a circle
# n < 2 * 10^9

# Output:
# The last digit of the number of greeting configurations.

def fibonacci_last_digit(n):
    period = 60
    n = n % period

    if n == 0:
        return 0
    elif n == 1:
        return 1

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10
    return current

def count_greetings(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    fib_n = fibonacci_last_digit(n )
    fib_n_minus_2 = fibonacci_last_digit(n - 2)
    
    return (fib_n + fib_n_minus_2) % 10

n = int(input())

print(count_greetings(n+1))
