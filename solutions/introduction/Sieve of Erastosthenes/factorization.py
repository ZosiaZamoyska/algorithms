# Problem: Prime Factorization
# The first line of input contains a natural number T (T <= 1000) – the number of numbers to factorize.
# Each of the next T lines contains a number n (2 <= n <= 10^9).
#
# For each number, output its prime factorization in the form:
# n = p1^a1 * p2^a2 * ... * pk^ak
# Omitting the exponent if it equals 1.
#
# Example Input:
# 3
# 30
# 36
# 404
#
# Example Output:
# 30 = 2*3*5
# 36 = 2^2*3^2
# 404 = 2^2*101
#
# https://szkopul.edu.pl/problemset/problem/7F7_ZR1sUvvTGMkqJIbFKx4K/site/?key=statement


def sieve(limit):
    F = [0] * (limit + 1)
    primes = []
    
    for i in range(2, limit + 1):
        if F[i] == 0:
            F[i] = i
            primes.append(i)
        for p in primes:
            if p * i > limit or p > F[i]:
                break
            F[p * i] = p
    
    return F

def prime_factorization(n, F):
    factors = {}
    
    while n > 1:
        prime = F[n]
        factors[prime] = factors.get(prime, 0) + 1
        n //= prime
    
    result = " * ".join(f"{p}^{e}" if e > 1 else f"{p}" for p, e in factors.items())
    return result

t = int(input())
max_n = 10**6
F = sieve(max_n)

for _ in range(t):
    n = int(input())
    print(f"{n} = {prime_factorization(n, F)}")