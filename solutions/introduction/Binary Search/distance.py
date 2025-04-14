'''
    For a set of queries (a, b) on a sorted array (arr), find largest distance between value a and b in the array.
'''

def lower_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

def upper_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left

def range_counts(arr, queries):
    results = []
    for a, b in queries:
        left = lower_bound(arr, a)
        right = upper_bound(arr, b) - 1
        if left <= right:
            #print(right-left)
            results.append(right - left)
        else:
            #print(0)
            results.append(0)
    return results

n, m = 9, 3
arr = [1, 2, 2, 3, 4, 4, 5, 7, 7]
queries = [(2, 4), (2, 7), (4, 7)]

print(*range_counts(arr, queries))
