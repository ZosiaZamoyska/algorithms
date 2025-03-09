''''
    Problem: Half-prime numbers
    A half-prime number is a number that is the product of exactly two prime numbers.
    We receive queries asking how many half-prime numbers exist in the range [a, b].
'''

def sieve_factorization(n):
    F = [0] * (n + 1)
    
    for i in range(2, int(n**0.5) + 1):
        if F[i] == 0:
            for k in range(i * i, n + 1, i):
                if F[k] == 0:
                    F[k] = i
    
    return F

def compute_half_primes(n, F):
    half_prime = [0] * (n + 1)
    prefix_sum = [0] * (n + 1)
    
    for i in range(2, n + 1):
        if F[i] != 0 and F[i // F[i]] == i // F[i]:
            half_prime[i] = 1
    
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + half_prime[i]
    
    return prefix_sum

def query_half_primes(a, b, prefix_sum):
    return prefix_sum[b] - prefix_sum[a - 1]

n = int(input())
factors = sieve_factorization(n)
prefix_sum = compute_half_primes(n, factors)

q = int(input())
for _ in range(q):
    a, b = map(int, input().split())
    print(query_half_primes(a, b, prefix_sum))
