'''
    Three solutions with different complexity: O(n^3), O(n^2), O(n).
'''
def max_sum_n3(n, arr):
    ans = 0
    for i in range(n):
        for j in range(i, n):
            sum = 0
            for k in range(i, j+1):
                sum += arr[k]
            ans = max(ans, sum)
    return ans
    
def max_sum_n2(n, arr):
    pref = [0]
    ans = 0
    for i in range(n):
        pref.append(pref[i]+arr[i])
    for i in range(n):
        for j in range(i, n):
            sum = pref[j+1] - pref[i]
            ans = max(ans, sum)
    return ans
    
def max_sum_n(n, arr):
    ans = 0
    w = [0] * (n+1)
    for i in range(n-1, -1, -1):
        w[i] = max(w[i+1]+arr[i], arr[i])
        ans = max(ans, w[i])
    return ans

n = int(input())
arr = list(map(int, input().split(' ')))
#n = 7
#arr = [5, -7, 3, 5, -2, 4, -1]
print(max_sum_n(n, arr))