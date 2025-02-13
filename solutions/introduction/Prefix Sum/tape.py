'''
    Given a tape with a list of n integers (1 <= n <= 1,000,000), a boy tries to find the minimum possible arithmetic mean of any contiguous subarray.
    Round the answer to second decimal point.
    
    Example
    3 4 2 2 2 5 8

    Output
    2.00

    (trick is to notice that the answer is just minimum value)
'''

def min_average_subarray(a):
    return round(min(a), 2)


a = list(map(int, input().split(' ')))  
# a = [3, 4, 2, 2, 2, 5, 8]

print(min_average_subarray(a))
