
n = int(input())
graph = [[] for _ in range(n)]
dp = [[0, 0] for _ in range(n)]  # dp[v][0] = sum of distances in subtree, dp[v][1] = final answer for node v
roz = [0] * n  # roz[v] = number of nodes in subtree rooted at v

# Read edges
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs1(v, parent):
    for u in graph[v]:
        if u != parent:
            dfs1(u, v)
            roz[v] += roz[u]
            dp[v][0] += dp[u][0] + roz[u]
    roz[v] += 1

def dfs2(v, parent, prev_val):
    print(v, parent, prev_val);
    dp[v][1] = dp[v][0] + prev_val + (n - roz[v])
    for u in graph[v]:
        if u != parent:
            # Recalculate the value passed to child based on the current node's value
            dfs2(u, v, dp[v][1] - (dp[u][0] + roz[u]))

dfs1(0, -1)
dfs2(0, -1, 0)

for i in range(n):
    print(dp[i][1])
