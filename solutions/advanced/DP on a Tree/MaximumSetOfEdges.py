n = int(input())
graph = [[] for _ in range(n + 1)]
dp = [[0, 0] for _ in range(n + 1)]
answer = 0

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dp_tree(v, prev):
    global answer
    for u in graph[v]:
        if u != prev:
            dp_tree(u, v)
            dp[v][0] += max(dp[u][0], dp[u][1])

    for u in graph[v]:
        if u != prev:
            dp[v][1] = max(dp[v][1], 1 + dp[u][0] + dp[v][0] - max(dp[u][0], dp[u][1]))

    answer = max(answer, max(dp[v][0], dp[v][1]))

# Assume root is 1
dp_tree(1, -1)
print(answer)
