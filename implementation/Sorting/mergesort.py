def merge(tab, p, m, q):
    a1 = m - p + 1
    a2 = q - m

    L = tab[p:p + a1]
    R = tab[m + 1:m + 1 + a2]

    i, j, k = 0, 0, p

    while i < a1 and j < a2:
        if L[i] <= R[j]:
            tab[k] = L[i]
            i += 1
        else:
            tab[k] = R[j]
            j += 1
        k += 1

    while i < a1:
        tab[k] = L[i]
        i += 1
        k += 1

    while j < a2:
        tab[k] = R[j]
        j += 1
        k += 1


def mergesort(tab, p, q):
    if p < q:
        m = (p + q) // 2
        mergesort(tab, p, m)
        mergesort(tab, m + 1, q)
        merge(tab, p, m, q)


n = int(input())
tab = list(map(int, input().split()))

mergesort(tab, 0, n - 1)

print(tab)


