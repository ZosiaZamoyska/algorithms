def selectionsort(tab):
    for i in range(len(tab)):
        minimum = i

        # find minimum in the un-sorted part of the array
        for j in range(i+1, len(tab)):
            if tab[j] < tab[minimum]:
                minimum = j

        # swap the minimum 
        tab[i], tab[minimum] = tab[minimum], tab[i]
    return tab


n = int(input())
tab = list(map(int, input().strip().split()))[:n]

print(selectionsort(tab))
