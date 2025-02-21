'''
    Three solutions with different complexity: O(n^6), O(n^4), O(n^3).
'''
def prefix_sum(n, arr):
    pref = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            pref[i][j] = (
                pref[i - 1][j]
                + pref[i][j - 1]
                - pref[i - 1][j - 1]
                + arr[i - 1][j - 1]
            )
    return pref

def column_prefix(n, arr):
    pref = [[0] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            pref[i][j] = pref[i-1][j] + arr[i-1][j-1]
    return pref

def max_sum_n(n, arr): # 1D array max subarray sum
    ans = 0
    w = [0] * (n+1)
    for i in range(n-1, -1, -1):
        w[i] = max(w[i+1]+arr[i], arr[i])
        ans = max(ans, w[i])
    return ans

def max_sum_n6(n, arr):
    ans = 0
    for x0 in range(n):
        for y0 in range(n):
            for x1 in range(x0, n):
                for y1 in range(y0, n):
                    # sum 
                    sum = 0
                    for i in range(x0, x1+1):
                        for j in range(y0, y1+1):
                            sum += arr[i][j]
                    ans = max(ans, sum)
    return ans

def max_sum_n4(n, arr):
    pref = prefix_sum(n, arr)

    for x0 in range(n):
        for y0 in range(n):
            for x1 in range(x0, n):
                for y1 in range(y0, n):
                    # sum 
                    sum = pref[x1][y1] 
                    - pref[x0 - 1][y1] 
                    - pref[x1][y0 - 1]
                    + pref[x0 - 1][y0 - 1]
                    ans = max(ans, sum)

    return ans
    

def max_sum_n3(n, arr):
    pref = column_prefix(n, arr)
    ans = 0
    
    for k in range(1, n+1):
        for i in range(0, n-k+1):
            w = [pref[i+k][j] - pref[i][j] for j in range(1, n+1)]
            sum = max_sum_n(n, w)
            ans = max(ans, sum)
    return ans
    

n = int(input())
arr = list(map(int, input().split(' ')))
#n = 3
#arr = [[5, -7, 3], [-1, 2, 2], [1, -1, 6]]
print(max_sum_n3(n, arr))