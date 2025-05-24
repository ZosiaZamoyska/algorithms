'''
A frog wants to jump from position 0 to position k using fixed jump lengths s0, s1, ..., sn-1.
It can only jump in the forward direction. Your task is to count how many different ways
the frog can reach exactly position k by making any number of jumps (including zero),
using the allowed jump distances.

Since the number of ways may be large, return the result modulo q.
'''

def count_ways_to_reach_k(n, k, s, q):
    dp = [0] * (k + 1)
    dp[0] = 1
    
    for j in range(1, k + 1):
        for i in range(n):
            if s[i] <= j:
                dp[j] = (dp[j] + dp[j - s[i]]) % q

    return dp[k]

n, k, q = map(int, input().split())
s = list(map(int, input().split()))

result = count_ways_to_reach_k(n, k, s, q)
print(result)
