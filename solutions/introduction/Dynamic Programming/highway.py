'''
In Bajtlandia, there are `n` cities located along a coastline. Each pair of consecutive cities
is connected by a one-way sandy road, and traveling along such a road takes exactly one day.

Additionally, from each city, there might be a one-way highway leading to another city.
Traveling via a highway also takes one day. However, due to the high cost, you are allowed to use
highways at most `k` times during the entire journey.

Michał wants to get from the first city (index 0) to the last city (index n-1) as quickly as possible.

You are given the number of cities `n`, the maximum allowed number of highway uses `k`,
and an array `m` of length `n` where:
- `m[i] == -1` means there is no highway from city i
- `m[i] == j` means there is a highway from city i to city j

Calculate the **minimum number of days** needed to travel from city 0 to city n-1,
using **at most `k` highways**.

Example:
Input:
6 1
2 -1 5 1 1 -1

Output:
3

Explanation:
City 0 → City 1 (sandy road)
City 1 → City 2 (sandy road)
City 2 → City 5 (highway)
'''

def min_days(n, k, m):
    dp = [[float('inf')] * n for _ in range(k + 1)]
    
    for j in range(n):
        dp[0][j] = j

    for i in range(1, k + 1):
        for j in range(n):
            dp[i][j] = dp[i - 1][j]

        for j in range(n):
            if m[j] != -1:
                dest = m[j]
                dp[i][dest] = min(dp[i][dest], dp[i - 1][j] + 1)

        for j in range(1, n):
            dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)

    return dp[k][n - 1]

n, k = map(int, input().split())
m = list(map(int, input().split()))

result = min_days(n, k, m)
print(result)
