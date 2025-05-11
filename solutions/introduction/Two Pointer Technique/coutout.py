'''
    Jasio found a very old roll of paper in the attic on which his great-grandfather had written a sequence of integers.
    For a game he recently invented, he needs a segment of the paper where the sum of all numbers is exactly `s`.
    He will throw away the unnecessary parts.
    Additionally, Jasio wants this segment to be as long as possible.

    Input:
    n, s <= 300,000
    a list of n integers (can be negative)

    Example:
    6 4
    3 -2 6 1 -1 5

    Output:
    4

    Explanation:
    The longest subarray that sums to 4 is: [-2, 6, 1, -1]
'''


def longest_subarray_with_sum(n, s, nums):
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    prefix_with_index = [(prefix[i], i) for i in range(n + 1)]
    prefix_with_index.sort()

    max_len = 0
    i = 0
    j = 0
    while j < len(prefix_with_index):
        current_diff = prefix_with_index[j][0] - prefix_with_index[i][0]
        if current_diff < s:
            j += 1
        elif current_diff > s:
            i += 1
        else:
            idx_i = prefix_with_index[i][1]
            idx_j = prefix_with_index[j][1]
            if idx_j > idx_i:
                max_len = max(max_len, idx_j - idx_i)
            j += 1

    return max_len

n, s = map(int, input().split())
nums = list(map(int, input().split()))

print(longest_subarray_with_sum(n, s, nums))
