def is_bst(w):
    n = len(w)
    min_vals = [float('-inf')] * n
    max_vals = [float('inf')] * n

    for i in range(1, n):
        left = 2 * i 
        right = 2 * i + 1

        if left < n:
            if not (min_vals[i] < w[left] < w[i]):
                return False
            min_vals[left] = min_vals[i]
            max_vals[left] = w[i]

        if right < n:
            if not (w[i] < w[right] < max_vals[i]):
                return False
            min_vals[right] = w[i]
            max_vals[right] = max_vals[i]

    return True

def is_bst_recursive(w):
    def check(i, min_val, max_val):
        if i >= len(w):
            return True
        if not (min_val < w[i] < max_val):
            return False
        left = 2 * i 
        right = 2 * i + 1
        return (check(left, min_val, w[i]) and
                check(right, w[i], max_val))

    return check(1, float('-inf'), float('inf'))

w = [0, 7, 4, 15, 1, 5, 10, 17] #-> YES

#w = [0, 7, 4, 15, 1, 8, 10, 17] #-> NO
print(is_bst(w))
print(is_bst_recursive(w))
