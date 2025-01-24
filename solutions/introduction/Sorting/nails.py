'''
    You are given a board with nails sticking out at different heights. Each nail has a specific sticking-out length. 
    Additionally, you are allowed to "nail" (reduce the height of) up to k nails, lowering them to any height less than or equal to their current height.
    
    The task is to determine the maximum number of nails that can stick out at the same height after using up to k nailing opportunities.

    Example:
    6 2 
    3 3 2 3 4 5

    Answer:
    5
'''

def count(tab):
    largest = max(tab)
    count = [0] * (largest+1)

    for i in range(len(tab)):
        count[tab[i]] += 1

    return max(count)

n, k = map(int, input().split())
tab = list(map(int, input().strip().split()))[:n]
print(count(tab[:-k]) + k)
