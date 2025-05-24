from collections import defaultdict

INF = int(1e9 + 21)
N = 55

t = int(input())
a = [0] * N
answer = -1

cost = [defaultdict(int) for _ in range(N)]
vis = {}

def compute_cost(index, val, curr_cost):
    cost[index][val] = curr_cost
    if val == 1:
        return

    if val % 2 == 1:
        if (val - 1) // 2 not in cost[index]:
            compute_cost(index, (val - 1) // 2, curr_cost + 1)
        if (val - 1) // 2 + 1 not in cost[index]:
            compute_cost(index, (val - 1) // 2 + 1, curr_cost + 1)
    else:
        if val // 2 not in cost[index]:
            compute_cost(index, val // 2, curr_cost + 1)

def find_min(val, n):
    global answer
    vis[val] = True
    total_cost = 0
    possible = True

    for i in range(n):
        curr_cost = cost[i].get(val, 0)
        if curr_cost == 0:
            possible = False
        total_cost += curr_cost - 1

    if possible:
        if answer == -1:
            answer = total_cost
        else:
            answer = min(answer, total_cost)

    if val == 1:
        return

    if val % 2 == 1:
        if not vis.get((val - 1) // 2, False):
            find_min((val - 1) // 2, n)
        if not vis.get((val - 1) // 2 + 1, False):
            find_min((val - 1) // 2 + 1, n)
    else:
        if not vis.get(val // 2, False):
            find_min(val // 2, n)

def clean(val):
    vis[val] = False
    if val % 2 == 1:
        if vis.get((val - 1) // 2, False):
            clean((val - 1) // 2)
        if vis.get((val - 1) // 2 + 1, False):
            clean((val - 1) // 2 + 1)
    else:
        if vis.get(val // 2, False):
            clean(val // 2)

def cost_clean(index, val):
    if val not in cost[index]:
        return
    cost[index][val] = 0
    if val == 1:
        return

    if val % 2 == 1:
        if cost[index].get((val - 1) // 2, 0):
            cost_clean(index, (val - 1) // 2)
        if cost[index].get((val - 1) // 2 + 1, 0):
            cost_clean(index, (val - 1) // 2 + 1)
    else:
        if cost[index].get(val // 2, 0):
            cost_clean(index, val // 2)

def solve(n):
    global answer
    min_a = a[0]
    for i in range(n):
        min_a = min(min_a, a[i])
        compute_cost(i, a[i], 1)

    find_min(min_a, n)
    clean(min_a)
    for i in range(n):
        cost_clean(i, a[i])

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    for i in range(n):
        a[i] = nums[i]

    solve(n)
    print(answer)
    answer = -1
    for i in range(n):
        a[i] = 0
