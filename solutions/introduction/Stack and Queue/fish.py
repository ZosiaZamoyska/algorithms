"""
Problem Statement:
There are N fish swimming in a river from east to west. Each fish swims one after another, 
some with the river current and some against it.

- If two fish swimming in opposite directions meet, the bigger fish eats the smaller one.
- Fish move at the same speed.
- No two fish have the same size.

Input:
- N (1 ≤ N ≤ 1,000,000) — number of fish.
- A[0], A[1], ..., A[N-1] — size of each fish (1 ≤ A[i] ≤ 10^9).
- K[0], K[1], ..., K[N-1] — direction of each fish (0 = with current, 1 = against current).

Output:
- Print the number of fish that will remain in the river.

Example:
Input:
5
4 3 2 1 5
0 1 0 0 0

Output:
2
"""

def remaining_fish(sizes, directions):
    stack = [] # store fishes going upstream
    survivors = 0

    for i in range(len(sizes)):
        size = sizes[i]
        direction = directions[i]

        if direction == 1:
            stack.append(size)
        else:
            while stack and stack[-1] < size:  # collisions between fishes going up and this fish
                stack.pop()
            if not stack:
                survivors += 1

    return survivors + len(stack)

n = int(input())
sizes = list(map(int, input().split()))
directions = list(map(int, input().split()))

print(remaining_fish(sizes, directions))
