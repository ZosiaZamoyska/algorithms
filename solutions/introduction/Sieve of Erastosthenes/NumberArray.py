#
# We are given an array containing n integers a0, a1, ..., an-1. 
# For each number ai, we want to count how many elements from the array are not divisors of it.
# n < 1,000,000
# a0, a1, ..., an-1 < 1,000,000
#
# Example input:
# 5
# 1 2 3 3 6
#
# Example output:
# 4 3 2 2 0
#
# Solution:
# The task can be solved in time O(n + k log k) where k is the maximum value in the array.
# First, we count the occurrences of each number in O(n) time.
# Then, we use a sieve-like approach. For each value in the array, we move through its multiples, 
# increasing the count of divisors for the respective cells. 
# Note that if we have multiple elements with the same value, we only check them once 
# thanks to the count array.

def solve(n, a):
    MAX_VAL = 1000000

    count = [0] * (MAX_VAL + 1)
    for num in a:
        count[num] += 1

    divisors_count = [0] * (MAX_VAL + 1)

    for i in range(1, MAX_VAL + 1):
        if count[i]:
            for j in range(i, MAX_VAL + 1, i):
                divisors_count[j] += count[i]

    result = []
    for num in a:
        result.append(n - divisors_count[num])

    return (" ".join(map(str, result)))

n = int(input())
a = list(map(int, input().split()))

print(solve(n, a))
