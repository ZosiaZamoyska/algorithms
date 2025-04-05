def power(a, b):
    if a == 0:
        return 0
    if b == 0:
        return 1
    return a * power(a, b - 1)

# Input
x = int(input())
n = int(input())

# Output
print(power(x, n))