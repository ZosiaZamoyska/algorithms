n = int(input())
tab = list(map(int, input().split()))

pref = [0] * n
pref[0] = tab[0]
for i in range(1, n):
    pref[i] = pref[i-1] + tab[i]
    
print(pref)