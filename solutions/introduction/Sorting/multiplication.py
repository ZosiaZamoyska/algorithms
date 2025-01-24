'''
    Find values x, y, z from a list, such that their product is as large as possible.
    Do it for m sets of queries. 
    Input: m (queries <= 10), for each query: n (elements in a list <=100,000) and then n values (-1000 <= x <= 1000).
     
    Example
    2
    5
    1 4 3 2 5
    4
    -2 1 1 5
    Answer
    60
5
'''

t = int(input())

for i in range(t):
    n = int(input())
    tab = list(map(int, input().strip().split()))[:n]

    sort_tab = sorted(tab)

    ans = max(sort_tab[n-3]*sort_tab[n-2]*sort_tab[n-1], sort_tab[0]*sort_tab[1]*sort_tab[n-1])
    print(ans)