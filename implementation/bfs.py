from collections import deque

N = 1000 * 1000 + 6
INF = 1000 * 1000 * 1000 + 33

as_ = [[] for _ in range(N)]
dis = [INF] * N

x, y = map(int, input().split())  # vertices and edges

for _ in range(y):
    from_, to = map(int, input().split())
    as_[from_].append(to)
    as_[to].append(from_)  # undirected graph

def bfs(a):
    for i in range(1, x + 1):
        dis[i] = INF
    q = deque()
    q.append(a)
    dis[a] = 0

    while q:
        curr = q.popleft()
        for i in as_[curr]:
            if dis[i] > dis[curr] + 1:
                dis[i] = dis[curr] + 1
                q.append(i)

bfs(1)

for i in range(1, x + 1):
    print(dis[i], end=' ')
