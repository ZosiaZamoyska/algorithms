# How many unique elements are in this array?

def unique(tab):
    count = 1
    for i in range(1, len(tab)):
        if tab[i] != tab[i-1]:
            count += 1
    return count

n = int(input())
tab = list(map(int, input().strip().split()))[:n]

# sort the inital array and count points where elements change
print(unique(sorted(tab)))
