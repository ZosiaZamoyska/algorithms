"""
We have an array of n numbers a0, a1, ..., a(n-1) (where ai is either 0 or 1).
- ai = 0 means a person joins the queue.
- ai = 1 means a person leaves the queue.

Our task is to determine the minimum number of people who had to be in the queue initially
so that this sequence of events is possible (i.e., there is never a moment when a person leaves an empty queue).

Example:
Input: n = 6
       arr = [1, 0, 1, 1, 0, 1]
Output: 2

"""

def min_initial_queue(arr):
    queue_size = 0
    min_queue_size = 0

    for num in arr:
        if num == 0:
            queue_size += 1
        else:
            queue_size -= 1
        min_queue_size = min(min_queue_size, queue_size)

    return -min_queue_size

n = int(input())
arr = list(map(int, input().split(' ')))
#arr = [1, 0, 1, 1, 0, 1]
print(min_initial_queue(arr))
