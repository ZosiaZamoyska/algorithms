'''
    8 8
    1 2
    2 3
    3 4
    1 6
    6 3
    3 7
    7 8
    8 4
'''

N = 1000 * 1000 + 6
lista = [[] for _ in range(N)]
vis = [False] * N
pre = [0] * N
post = [0] * N
counter_pre = 1
counter_post = 1

def dfs(curr):
    vis[curr] = True
    pre[counter_pre] = curr
    counter_pre += 1

    for i in lista[curr]:
        if not vis[i]:
            dfs(i)

    post[counter_post] = curr
    counter_post += 1

x, y = map(int, input().split())
for _ in range(y):
    from_, to = map(int, input().split())
    lista[from_].append(to)
    lista[to].append(from_)

dfs(1)

print(' '.join(str(pre[i]) for i in range(1, x + 1)))
print(' '.join(str(post[i]) for i in range(1, x + 1)))
