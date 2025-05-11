'''
    We are given temperature readings from two thermometers: one on the north wall and one on the south wall.
    - The north wall thermometer *never shows higher* than the actual temperature.
    - The south wall thermometer *never shows lower* than the actual temperature.
    This means the true temperature on day i lies within the interval [north[i], south[i]].

    Return the length of the **longest contiguous time interval** (subarray) during which it was *possible* that the actual temperatures were **non-decreasing**.

    Constraints:
    - 1 <= n <= 1,000,000
    - -1e9 <= north[i] <= south[i] <= 1e9

    Example:
    6
    6 10
    1 5
    4 8
    2 5
    6 8
    3 5

    Output:
    4

    Explanation:
    The longest range where some non-decreasing sequence of possible actual temperatures could exist is of length 4.
'''

from collections import deque

def longest_non_decreasing_interval(n, intervals):
    x = [a for a, b in intervals]
    y = [b for a, b in intervals]

    max_x = deque()
    min_y = deque()

    res = 0
    left = 0

    for right in range(n):
        while max_x and x[right] > max_x[-1]:
            max_x.pop()
        max_x.append(x[right])

        while min_y and y[right] < min_y[-1]:
            min_y.pop()
        min_y.append(y[right])

        while max_x[0] > min_y[0]:
            if max_x[0] == x[left]:
                max_x.popleft()
            if min_y[0] == y[left]:
                min_y.popleft()
            left += 1

        res = max(res, right - left + 1)

    return res

n = 6
intervals = [
    (6, 10),
    (1, 5),
    (4, 8),
    (2, 5),
    (6, 8),
    (3, 5)
]

print(longest_non_decreasing_interval(n, intervals))
