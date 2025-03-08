#
# To prove that you can quickly find prime numbers, calculate the sum of prime numbers in the interval [a, b], 
# for various given a and b.
#
# The first line of input contains a natural number T ≤ 100,000, the number of intervals you must process. 
# In the following T lines, there are pairs of natural numbers (ai, bi) separated by a space. 
# It is guaranteed that 2 ≤ ai ≤ bi ≤ 2,000,000.
#
# For the input:
# 3
# 2 10
# 20 100
# 48 52
#
# The correct output is:
# 17
# 983
# 0
# https://szkopul.edu.pl/problemset/problem/L_KYSGXAxJc-wNVa54AtSdH7/site/?key=statement

def sieve_and_prefix_sum(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0], is_prime[1] = False, False
    
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    
    prefix_sum = [0] * (limit + 1)
    for i in range(1, limit + 1):
        prefix_sum[i] = prefix_sum[i - 1] + (i if is_prime[i] else 0)
    
    return prefix_sum

T = int(input())

MAX_LIMIT = 2000000

prefix_sum = sieve_and_prefix_sum(MAX_LIMIT)

for _ in range(T):
    a, b = map(int, input().split())
    print(prefix_sum[b] - prefix_sum[a - 1])
