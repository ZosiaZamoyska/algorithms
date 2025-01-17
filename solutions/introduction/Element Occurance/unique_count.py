'''
    Check if element count of elements is unique. 

    [1, 2, 2, 3, 3, 3] each count is unique.

    [1, 2] both elements have same count, so it is not unique.

'''

def has_unique_counts(arr):
    count_dict = {}

    for num in arr:
        count_dict[num] = count_dict.get(num, 0) + 1

    return len(set(count_dict.values())) == len(count_dict.values())


arr = list(map(int, input().split(' ')))
print(has_unique_counts(arr))

#print(has_unique_counts([1, 2, 2, 3, 3, 3]))  # Output: True (counts: {1:1, 2:2, 3:3})
#print(has_unique_counts([1, 2]))  # Output: False (counts: {1:1, 2:1})
#print(has_unique_counts([4, 4, 4, 4, 5, 5, 5, 6, 6]))  # Output: True (counts: {4:4, 5:3, 6:2})
#print(has_unique_counts([7, 8, 9, 10, 10, 9, 8, 7]))  # Output: False (counts: {7:2, 8:2, 9:2, 10:2})
