# 
# Three boys each have coins of denominations a, b, and c respectively (each boy has only one type of coin).
# They want to find the smallest possible amount of money that each of them can pay using only their coins.
#

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

def lcm(x, y):
    return x * y // gcd(x, y)

a, b, c = map(int, input().split())
result = lcm(a, lcm(b, c))
print(result)
