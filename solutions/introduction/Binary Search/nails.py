'''
    Find minimum number of nails that need to be nailed in order for all plates to be nailed. You are given plate start and end point, and nail locations in order of nailing.
    One nail can nail more than one plate.
'''

def is_all_nailed(boards, nails, k):
    max_pos = max(max(end for start, end in boards), max(nails[:k]))
    nailed = [0] * (max_pos + 2)

    for i in range(k):
        nailed[nails[i]] += 1

    for i in range(1, len(nailed)):
        nailed[i] += nailed[i - 1]

    for start, end in boards:
        if nailed[end] - nailed[start - 1] == 0:
            return False
    return True

def min_nails_needed(boards, nails):
    left, right = 1, len(nails)
    answer = -1
    while left <= right:
        mid = (left + right) // 2
        if is_all_nailed(boards, nails, mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer

boards = [(1, 4), (4, 5), (5, 9), (8, 10)]
nails = [4, 6, 7, 10, 2]

print(min_nails_needed(boards, nails))  # Output: 4
