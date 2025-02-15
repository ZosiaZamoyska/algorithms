"""
A flag consists of `n` horizontal stripes, each with a different color. The king wants to change the flag so that it consists of `n` stripes in only two alternating colors (A and B). 
The goal is to minimize the number of stripes that need to be repainted. The choice of colors does not matter, but the colors must alternate.

Example:
Input:
6
1 2 3 1 4 2

Output:
3
New colors: 1, 2, 1, 2, 1, 2
"""

def count_frequencies(arr, start, step):
    freq = {}

    first_color, first_count = -1, 0
    second_color, second_count = -1, 0

    for i in range(start, len(arr), step):
        color = arr[i]
        freq[color] = freq.get(color, 0) + 1
        if freq[color] > first_count:
            if color == first_color:
                first_count = freq[color]
            else:
                second_color, second_count = first_color, first_count
                first_color, first_count = color, freq[color]
        elif freq[color] > second_count:
            second_color, second_count = color, freq[color]
    return first_color, first_count, second_color, second_count

def min_repaints(n, colors):
    even1_color, even1_count, even2_color, even2_count = count_frequencies(colors, 0, 2)
    odd1_color, odd1_count, odd2_color, odd2_count = count_frequencies(colors, 1, 2)


    ans1, ans2, ans3 = float('inf'), float('inf'), float('inf')
    if even1_color != odd1_color:
        ans1 = n - even1_count - odd1_count
    if even2_color != odd1_color:
        ans2 = n - even2_count - odd1_count
    if even1_color != odd2_color:
        ans3 = n - even1_count - odd2_count
    
    return min(ans1, ans2, ans3)

#n = 6
#colors = [1, 2, 3, 1, 4, 2]
n = int(input())
colors = list(map(int, input().split())) 

repaints = min_repaints(n, colors)
print(repaints)