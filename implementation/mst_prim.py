def prim():
    start = 0
    visited = [False] * (n + 1)
    mst_edges = []

    Q = [(0, start, start)]

    while Q:
        weight, curr_v, from_v = heapq.heappop(Q)
        if visited[curr_v]:
            continue
        visited[curr_v] = True
        if from_v != curr_v:
            mst_edges.append(((from_v, curr_v), weight))

        for neighbor, edge_weight in graph[curr_v]:
            if not visited[neighbor]:
                heapq.heappush(Q, (edge_weight, neighbor, curr_v))

    return mst_edges