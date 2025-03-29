#
# A rabbit is jumping on a straight path using Fibonacci number lengths as jumps.
# Some positions contain stones where the rabbit cannot land.
# The rabbit wants to reach position 'n' from position 0 with the minimum number of jumps.
# The rabbit always jumps forward and cannot overshoot 'n'.
#
# Input:
# - An integer n (final position to reach)
# - A list of (n+1) integers where 0 indicates a free position, and 1 indicates a stone.
#
# Output:
# - The minimum number of jumps required to reach 'n', or -1 if impossible.
#
# Example:
# Input:
# 12
# 0 1 1 1 0 0 1 0 1 1 1 1 0
# Output:
# 3


def min_fib_jumps(n, obstacles):
    
    fib = [1, 2]
    while fib[-1] + fib[-2] <= n:
        fib.append(fib[-1] + fib[-2])
    
    jumps = [n+1] * (n + 1)
    
    if obstacles[0] == 0:
        jumps[0] = 0
    
    for k in range(1, n + 1):
        if obstacles[k] == 0:
            for f in fib:
                if k - f >= 0:
                    jumps[k] = min(jumps[k], jumps[k - f] + 1)
    
    return jumps[n] if jumps[n] <= n else -1


n = int(input())
obstacles = list(map(int, input().split()))

#n = 12
#obstacles = [0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0]

print(min_fib_jumps(n, obstacles))  # Output: 3
