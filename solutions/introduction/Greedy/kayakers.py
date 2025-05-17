''''
We have `n` kayakers, each with a weight such that 1 <= w_0 <= w_1 <= ... <= w_(n-1) <= 10^9.
We want to assign them to the minimum number of two-person kayaks with a weight capacity of `k`. 
Each kayak can hold up to two people as long as their combined weight does not exceed `k`. 
It is guaranteed that each individual weighs less than or equal to `k`, so everyone can go alone if necessary.
'''

def min_kayaks(weights, k):
    weights.sort()
    i, j = 0, len(weights) - 1
    kayaks = 0

    while i <= j:
        if weights[i] + weights[j] <= k:
            i += 1
        j -= 1
        kayaks += 1

    return kayaks

# Example usage:
weights = [1, 2, 3, 4, 5]
k = 5
print(min_kayaks(weights, k))  # Output: 3
