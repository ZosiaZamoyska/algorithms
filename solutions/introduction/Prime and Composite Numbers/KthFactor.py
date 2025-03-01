'''
    You are given two positive integers n and k. 
    A factor of an integer n is defined as an integer i where n % i == 0.
    Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.

    https://leetcode.com/problems/the-kth-factor-of-n/description/
'''

def kth_factor_n(n, k):
    count = 0
    for i in range(1, int(n**0.5)+1):
            print(i)
            if n % i == 0:
                count += 1
            if count == k:
                return i
    for i in range(int(n**0.5)-1, 0, -1):
        print(i)
        if n % i == 0:
            count += 1
        if count == k:
            return n/i
    return -1

def kth_factor(n, k):
    factors = []
    large_factors = []

    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i: 
                large_factors.append(n // i)

    all_factors = factors + large_factors[::-1]
    return all_factors[k - 1] if k <= len(all_factors) else -1


n = int(input())
k = int(input())

print(kth_factor(n, k))