'''
    Find smallest amount, such that a list can be divided into k segments where each segment's sum does not exceed this amount.

    For example, [7, 2, 5, 10, 8] can be divided into k=2 segments where each segment does not exceed 18.
    Find smallest number. 
'''

def can_split(nums, k, max_sum_allowed):
    count = 1
    current_sum = 0

    for num in nums:
        if current_sum + num > max_sum_allowed:
            count += 1
            current_sum = num
        else:
            current_sum += num

    return count <= k


def minimize_largest_segment_sum(nums, k):
    left = max(nums)
    right = sum(nums)

    while left < right:
        mid = (left + right) // 2
        if can_split(nums, k, mid):
            right = mid
        else:
            left = mid + 1

    return left


a = [7, 2, 5, 10, 8]
k = 2
print(minimize_largest_segment_sum(a, k))
