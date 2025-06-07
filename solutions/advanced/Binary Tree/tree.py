'''
    We are given a binary tree of height k. Each edge can be closed or open. Initially, all left edges are open. The boy drops n balls one by one. The balls fly from the starting vertex, which is the root of the tree, through an open edge. A ball flying through a given edge closes it and opens the adjacent edge.
    The boy wonders which leaf the n-th ball will fall into.
    We read the number of balls and the height of the tree. (N <= 10^8, 1 <= k <= 31)

    Example
    4 3
    Answer
    3
    (0, 2, 1, 3)
'''

def simulate(n, k):
    start = 0
    end = (1 << k-1) - 1
    n -= 1
    for i in range(k-1):
        middle = (start + end) // 2
        if n % 2 == 0:
            end = middle
        else:
            start = middle + 1
        n //= 2
    return start

def calculate(n, k):
    n -= 1
    ans = 0
    for i in range(k-1):
        ans = 2 * ans + n%2
        n //= 2
    return ans

n, k = map(int, input().split())
print(calculate(n, k))