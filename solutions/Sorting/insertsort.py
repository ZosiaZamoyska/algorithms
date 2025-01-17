def insertsort(tab):
    for i in range(1, len(tab)):
        val = tab[i]
        j = i-1

        while j>=0 and tab[j] > val:
            tab[j+1] = tab[j] 
            j -= 1
        tab[j+1] = val
    return tab

n = int(input())
tab = list(map(int, input().strip().split()))[:n]

print(insertsort(tab))
