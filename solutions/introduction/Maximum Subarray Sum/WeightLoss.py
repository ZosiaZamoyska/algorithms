'''
    A boy has been on a mission to lose weight. He noted his weight everyday in a diary.
    He wants to brag to his friends, but he wants to chose a segment of his diary that makes him look best.
    Find a segment of the weight entries where the boy lost the most weight and print out the difference.

    For example
    5
    6 7 5 4 2

    Answer is 5
    Since the boy lost most on segment [7, 5, 4, 2].
'''
def max_weight_loss(n, arr):
    max_weight = 0
    ans = 0
    for i in range(n):
        max_weight = max(max_weight, arr[i])
        ans = max(ans, max_weight - arr[i])
    return ans
 
n = int(input())
arr = list(map(int, input().split())) 

print(max_weight_loss(n, arr))