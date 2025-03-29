#
# Given a list of numbers x0, x1, ..., xm, check whether each number can be expressed 
# as the sum of two Fibonacci numbers.
#
# Constraint:
# - m < 1,000,000
#

def generate_fibonacci(limit):
    fib = [1, 1]
    while fib[-1] + fib[-2] <= limit:
        fib.append(fib[-1] + fib[-2])
    return fib

def precompute_sums(fib):
    fib_sums = set()
    for i in range(len(fib)):
        for j in range(i, len(fib)):
            fib_sums.add(fib[i] + fib[j])
    return fib_sums

LIMIT = 1000000
fib_numbers = generate_fibonacci(LIMIT)

fib_sums = precompute_sums(fib_numbers)

data = list(map(int, input().split()))

print(fib_sums)
for x in data:
    if x in fib_sums:
        print("YES")
    else:
        print("NO")
