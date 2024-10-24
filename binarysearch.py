n = 5
arr = [3, 6, 7, 13, 15]
# binary search div function 
# true - go left comp
# false - go right comp
def func(curr, query):
    return curr >= query

def binarySearch(left, right, query):
    while (left < right):
        mid = (left + right) // 2
        if func(arr[mid], query):
            right = mid
        else:
            left = mid + 1
    return left

ans = binarySearch(0, n, 8)
print(ans)
