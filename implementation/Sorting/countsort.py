def countsort(tab):
    largest = max(tab)
    count = [0] * (largest+1)
    
    for i in range(len(tab)):
        count[tab[i]] += 1
    
    ans = []
    for i in range(largest+1):
        ans.extend([i] * count[i])
    return ans


n = int(input())
tab = list(map(int, input().strip().split()))[:n]

print(countsort(tab))
