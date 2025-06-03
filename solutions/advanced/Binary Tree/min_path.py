'''
    For a given binary tree, find a path with minum sum from root to a leaf.

    Example:
    3 8 4 6 3 0 12 11 6 4 10 12 7 11 10

    Output:
    14


'''
def min_leaf_to_root_sum(w):
    n = len(w) 
    min_sum = [0] * (n + 1)

    for i in range(n // 2 + 1, n + 1):
        min_sum[i] = w[i]

    for i in range(n // 2, 0, -1):
        left = 2 * i
        right = 2 * i + 1
        min_sum[i] = w[i] + min(min_sum[left], min_sum[right])

    return min_sum[1]

print(min_leaf_to_root_sum([0, 3, 8, 4, 6, 3, 0, 12, 11, 6, 4, 10, 12, 7, 11, 10]))