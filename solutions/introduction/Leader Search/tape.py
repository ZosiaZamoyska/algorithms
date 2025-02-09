'''
A boy found a long tape at home and, without hesitation, wrote a sequence of integers on it. He wants to cut the tape in some places, but there is a strict condition:
A cut can only be made if both parts of the tape have the same leader.
A leader of a sequence is an element that appears more than half the times in that sequence.
Your task is to determine the number of valid cut positions where both the left and right parts of the tape have the same leader.

The first line contains an integer N (1 ≤ N ≤ 1,000,000) — the length of the sequence.
The second line contains N integers (each between -10⁹ and 10⁹) representing the sequence.

Example
6
4 3 4 4 4 2
Output
2
'''

def find_leader(arr):
    candidate, count = None, 0

    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        else:
            count += 1 if num == candidate else -1

    leader_count = arr.count(candidate)
    if leader_count > len(arr) // 2:
        return candidate, leader_count 
    return None, 0


def count_valid_cuts(arr):
    n = len(arr)
    leader, leader_count = find_leader(arr)

    if leader is None:
        return 0 

    left_count, valid_cuts = 0, 0
    for i in range(n - 1):
        if arr[i] == leader:
            left_count += 1
        left_size = i + 1
        right_size = n - left_size
        if left_count > left_size // 2 and (leader_count - left_count) > right_size // 2:
            valid_cuts += 1

    return valid_cuts


n = int(input())  
arr = list(map(int, input().split())) 

print(count_valid_cuts(arr))
