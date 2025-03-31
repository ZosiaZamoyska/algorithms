# 
# We are given two integers a and b. We want to check whether the set of prime divisors of a 
# is a subset of the set of prime divisors of b. The set of prime divisors of a number includes 
# every prime number that divides it.
#
# For example, the prime divisors of 75 are {3, 5}.
#
# Input:
# - The first line contains an integer t, the number of test cases.
# - Each of the next t lines contains two integers a and b.
#
# Output:
# - "YES" if all prime factors of a are in the set of prime factors of b.
# - "NO" otherwise.
#
# Example:
# Input:
# 3
# 2 3
# 2 4
# 4 10
#
# Output:
# NO
# YES
# YES


def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

def czy_podzbior(a, b):
    gcd_ab = gcd(a, b)

    while a > 1:
        gcd_ab = gcd(a, b)
        if gcd_ab == 1:
            return "NO"
        a //= gcd_ab

    return "YES"

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(czy_podzbior(a, b))
