'''
    Given two nodes in an infinite binary tree, find the distance between them. Consider root node to be 1. Distance is defined by number of edges between them, where each edge is of length 1. 
    a, b <= 2*10^9
'''

def distance(a, b):
    ans = 0 
    while a != b:
        if a < b: 
            b //= 2
        else:
            a //= 2
        ans += 1
    return ans 


a, b = map(int, input().split())
print(distance(a, b))
