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

def prime_factorization(n):
    factors = []
    k = n
    i = 2
    while i * i <= n:
        count = 0
        while k % i == 0:
            k //= i
            count += 1
        if count > 0:
            factors.append((i, count))
        i += 1
    if k > 1:
        factors.append((k, 1))
    return factors    

t = int(input())
for _ in range(t):
    n = int(input())
    factors = prime_factorization(n)
    result = f"{n} = "
    for idx, (factor, count) in enumerate(factors):
        if idx > 0:
            result += "*"
        result += f"{factor}"
        if count > 1:
            result += f"^{count}"
    print(result)