def count(tab):
    largest = max(tab)
    count = [0] * (largest+1)

    for i in range(len(tab)):
        count[tab[i]] += 1

    return max(count)

n, k = map(int, input().split())
tab = list(map(int, input().strip().split()))[:n]
print(count(tab[:-k]) + k)
