# Find three numbers with indexes x, y, z whose product is as large as possible

'''
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