'''
A girl placed n treats in a row. Each treat is of a certain type. 
The girl can now choose a certain number (from 1 to n) of consecutive treats and then eat them all. 
The only condition is that no two treats can be of the same type. 
Help the girl and find the number of ways in which she can choose such consecutive treats.

Input:
N, m <= 300,000
C0, C1, ..., Cn <= m

Example:
5 3
1 3 2 2 3

Output:
9
'''

def count_unique_treats(n, m, treats):
    count = {}
    left = 0
    result = 0

    for right in range(n):
        while treats[right] in count and count[treats[right]] > 0:
            count[treats[left]] -= 1
            left += 1
        count[treats[right]] = count.get(treats[right], 0) + 1
        result += (right - left + 1)
    
    return result

n, m = map(int, input().split())
treats = list(map(int, input().split()))

print(count_unique_treats(n, m, treats))
