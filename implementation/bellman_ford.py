INF = int(1e9) + 21
N = 1000 + 21

n, m = map(int, input().split())
dist = [INF] * (N)
edges = []

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append(((a, b), c))

def bellman_ford(start):
    dist[start] = 0

    for _ in range(n - 1):
        for (u, v), weight in edges:
            if dist[u] != INF and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight

    # Check for negative-weight cycles
    for (u, v), weight in edges:
        if dist[u] != INF and dist[u] + weight < dist[v]:
            return False
    return True

if bellman_ford(1):
    for i in range(1, n + 1):
        if dist[i] == INF:
            print("INF", end=" ")
        else:
            print(dist[i], end=" ")
    print()
else:
    print("Contains negative cycle")
