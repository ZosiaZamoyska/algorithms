#
# A boy climbs a ladder. He can take either one step or two steps at a time.
# We want to determine the number of different ways he can reach the top of the ladder.
# Since the number of ways can be very large, we only need to return the result modulo 2^p.
#
# Input:
# Z - Number of test cases (Z < 1,000,000)
# For each test case, two integers S and p (1 <= S <= 1,000,000, p < 30)
#
# Output:
# The number of ways to reach the top of the ladder (modulo 2^p) for each test case.


def compute_ways(limit, max_p):
    mod = 1 << max_p
    ways = [0] * (limit + 1)
    ways[0] = 1
    ways[1] = 1
    
    for i in range(2, limit + 1):
        ways[i] = (ways[i - 1] + ways[i - 2]) % mod
    
    return ways

z = int(input())

max_s = 1000000
max_p = 30
queries = []

ways = compute_ways(max_s, max_p)

for i in range(z):
    s, p = map(int, input().split())
    queries.append((s, p))
    print(ways[s] % (1 << p))


