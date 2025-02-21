'''
You are given an array of length `n`. A **leader** of an array is an element that appears 
in **more than half** of the array's elements. A **prefix leader** is an element that is a leader 
in more than `n/2` of the prefixes of the given array.

Your task is to find the **prefix leader** of the array. If no such element exists, return `-1`.

Input:
- An integer `n` (1 ≤ n ≤ 100,000) representing the length of the array.
- An array of `n` integers (1 ≤ arr[i] ≤ 10^9) representing the sequence.

Output:
- An integer representing the **prefix leader** of the sequence, or `-1` if no such leader exists.

Example:
Input:
9
3 4 5 3 3 1 3 3 3

Output:
3

Explanation:
The leader for each prefix (when it exists) is:
[3, -1, -1, 3, 3, -1, 3, 3, 3]
Since `3` is the leader in **more than 9/2 = 4.5** prefixes, it is the prefix leader.
'''
def find_prefix_leader(n, arr):
    candidate, count = None, 0
    leader_candidates = []
    prefix_counts = {}
    prefix_leader_count = {}

    for i in range(n):
        num = arr[i]
        prefix_counts[num] = prefix_counts.get(num, 0) + 1

        if count == 0:
            candidate = num
            count = 1
        else:
            count += 1 if num == candidate else -1

        if prefix_counts[candidate] > (i + 1) // 2:
            leader_candidates.append(candidate)
            prefix_leader_count[candidate] = prefix_leader_count.get(candidate, 0) + 1
        else:
            leader_candidates.append(-1)

    candidate, count = None, 0
    for num in leader_candidates:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    if candidate == -1 or prefix_leader_count.get(candidate, 0) <= n // 2:
        return -1

    return candidate

n = int(input())
arr = list(map(int, input().split()))
#n = 9
#arr = [4, 3, 5, 3, 3, 1, 3, 3, 3]
print(find_prefix_leader(n, arr))
