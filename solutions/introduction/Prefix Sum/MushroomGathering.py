'''
    Maximum Mushrooms Collection
    Given a list of n integers (1 <= n <= 100,000), where each value represents the number of mushrooms at that position along a path.
    A gatherer stands at position k and can make m moves (each move is left or right). Find the maximum mushrooms that can be collected.
'''

def max_mushrooms(a, k, m):
    n = len(a)
    prefix_sum = [0] * (n + 1)
    
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + a[i]
    
    max_collected = 0
    
    for i in range(min(m, k) + 1):
        left_pos = k - i
        remaining_moves = m - 2 * i
        right_pos = min(n - 1, max(k, k + remaining_moves))
        max_collected = max(max_collected, prefix_sum[right_pos + 1] - prefix_sum[left_pos])
    
    for i in range(min(m, n - k - 1) + 1):
        right_pos = k + i
        remaining_moves = m - 2 * i
        left_pos = max(0, min(k, k - remaining_moves))
        max_collected = max(max_collected, prefix_sum[right_pos + 1] - prefix_sum[left_pos])
    
    return max_collected

'''
a = [2, 3, 7, 5, 1, 3, 9]
k = 4
m = 6
# Output: 25
'''
k = int(input())
m = int(input())
a = list(map(int, input().split(' ')))
print(max_mushrooms(a, k, m))
