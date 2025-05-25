N = 1000000 + 21
tab = [[] for _ in range(N)]
dis = [[0, 0] for _ in range(N)]

def dfs(v, p, d, dlu):
    dis[v][dlu] = d
    node = -1
    for w in tab[v]:
        if w != p:
            x = dfs(w, v, d + 1, dlu)
            if node == -1 or dis[x][dlu] > dis[node][dlu]:
                node = x
    if node == -1:
        return v
    return node


n = int(input())
for _ in range(n-1):
    a, b = map(int, input().split())
    tab[a].append(b)
    tab[b].append(a)

A = dfs(1, 1, 0, 0)
B = dfs(A, A, 0, 0)

print(f"Diameter is from {A} to {B}")


