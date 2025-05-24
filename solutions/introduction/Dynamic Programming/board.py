'''
A girl received a board with `n` fields, each containing an integer: p0, p1, ..., p(n-1).
A boy came up with a game:

Starting from position 0, you must move a token to position n-1 by rolling a six-sided die.
Each move lets you jump 1 to 6 fields forward.

The goal is to collect the highest possible total by summing the values of all visited fields,
starting from position 0 and ending at position n-1.

Return the maximum sum you can get by playing optimally.

Example:
Input:
5
3 1 -2 -1 3

Output:
7
(Explanation: 3 → 1 → 3 is the optimal path, skipping negative values)
'''

def max_sum_on_board(p):
    n = len(p)
    dp = [float('-inf')] * n
    dp[0] = p[0]

    for i in range(1, n):
        for k in range(1, 7):
            if i - k >= 0:
                dp[i] = max(dp[i], dp[i - k])
        dp[i] += p[i]

    return dp[n - 1]


n = int(input())
p = list(map(int, input().split()))

result = max_sum_on_board(p)
print(result)
