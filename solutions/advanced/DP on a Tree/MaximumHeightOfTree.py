n = int(input())
graph = [[] for _ in range(n + 1)]
in_depth = [0] * (n + 1)
out_depth = [0] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs_in(v, parent):
    max_depth = 0
    for neighbor in graph[v]:
        if neighbor != parent:
            max_depth = max(max_depth, dfs_in(neighbor, v) + 1)
    in_depth[v] = max_depth
    return max_depth

def dfs_out(v, parent):
    # First and second max in-depths among children
    max1 = max2 = 0
    for neighbor in graph[v]:
        if neighbor != parent:
            if in_depth[neighbor] >= max1:
                max2 = max1
                max1 = in_depth[neighbor]
            elif in_depth[neighbor] > max2:
                max2 = in_depth[neighbor]

    for neighbor in graph[v]:
        if neighbor != parent:
            use = max1
            if in_depth[neighbor] == max1:
                use = max2
            out_depth[neighbor] = max(out_depth[v], use + 1) + 1
            dfs_out(neighbor, v)

dfs_in(1, -1)
dfs_out(1, -1)

max_height = 0
for i in range(1, n + 1):
    max_height = max(max_height, max(in_depth[i], out_depth[i]))

print(max_height)
