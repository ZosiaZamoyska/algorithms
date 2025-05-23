'''
Exercise: Siblings in a Line

There are `n` boys standing in a line. Some of them are brothers (belonging to the same family).
We want to remove some boys so that **the remaining siblings from any given family are all adjacent**.

Important rule: **If one boy is removed, all his brothers must also be removed.**
So we can only keep a family if all its members stand next to each other.

Goal: Compute the **maximum number of such families** that can remain in the line,
satisfying the above condition.

Example:
Input:
6  
1 2 1 2 3 2

Output:
2

Explanation:
- Family 1: indexes 0, 2 → not contiguous
- Family 2: indexes 1, 3, 5 → not contiguous
- Family 3: index 4 → singleton

After selecting family 2 starting at index 3 to 5, and family 3 at index 4 (which fits between others), we can keep 2 families.
'''

def max_non_overlapping_families(n, ids):

    first = {}
    last = {}

    for i, fam in enumerate(ids):
        if fam not in first:
            first[fam] = i
        last[fam] = i

    intervals = [(first[fam], last[fam]) for fam in first]
    intervals.sort(key=lambda x: x[1])

    result = 0
    prev_end = -1

    for start, end in intervals:
        if start > prev_end:
            result += 1
            prev_end = end

    return result

# Example usage:
n = 6
ids = [1, 2, 1, 2, 3, 2]
print(max_non_overlapping_families(n, ids))  # Output: 2
