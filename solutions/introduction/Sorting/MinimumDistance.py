'''
In a city, railway tracks run in a straight line from east to west. The houses of the residents are located to the north of the railway track.
If two people from different houses want to meet, they meet at the midpoint of the distance between their houses. However, this distance is not calculated in a traditional way as a straight-line segment between the houses.
Instead, the distance is determined as follows: a person first walks south to the railway tracks, then along the tracks to the line where the target house is located, and finally walks straight north to that house.
From all possible pairs of houses, we want to find the pair for which this distance is minimal.

Input:
- N (2 <= N <= 1,000,000), xi, yi (1 <= xi, yi <= 10^9).

Example Input:
3
1 1
2 2
3 3

Output:
4
'''


def min_meeting_distance(houses):
    houses.sort()
    
    min_distance = float('inf')
    min_distance = float('inf')
    prev_x, prev_y = houses[0]

    for i in range(1, len(houses)):
        x, y = houses[i]
        distance = abs(x - prev_x) + prev_y + y
        min_distance = min(min_distance, distance)
        if y < prev_y + (x - prev_x):
            prev_x, prev_y = x, y 
    
    return min_distance

n = int(input())
houses = [tuple(map(int, input().split(' '))) for _ in range(n)]

print(min_meeting_distance(houses))

