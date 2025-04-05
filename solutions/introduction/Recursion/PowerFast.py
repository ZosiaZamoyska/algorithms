def power(a, b):
    if a == 0:
        return 0
    if b == 0:
        return 1
    curr = power(a, b // 2)
    if b % 2:
        return a * curr * curr
    else:
        return curr * curr

# Input
x = int(input())
n = int(input())

# Output
print(power(x, n))
