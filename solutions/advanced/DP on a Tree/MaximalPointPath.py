n = int(input())
graph = [[] for _ in range(n + 1)]
dp = [0] * (n + 1)
vis = [0] * (n + 1)
points = [0] * (n + 1)
ans = 0

# Read point values
for i in range(1, n + 1):
    points[i] = int(input())

# Read edges (a, b, cost)
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dfs(v):
    global ans
    vis[v] = 1
    max1 = 0
    max2 = 0

    for neighbor, weight in graph[v]:
        if not vis[neighbor]:
            dfs(neighbor)
        cost = dp[neighbor] - weight
        if cost >= max1:
            max2 = max1
            max1 = cost
        elif cost > max2:
            max2 = cost

    ans = max(ans, max1 + max2 + points[v])
    dp[v] = max1 + points[v]

dfs(1)
print(ans)
