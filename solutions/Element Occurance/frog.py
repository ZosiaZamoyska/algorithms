"""
  A small frog wants to cross a river by jumping on leaves that fall into 
  the river from a nearby tree. Initially, the frog is at position 0 and 
  wants to reach position n.

  We want to determine after which falling leaf the frog will be able 
  to safely jump across the river. The frog can only cross if leaves 
  have fallen on all positions from 1 to n.

  Input:
  - The first line of input contains two integers n, m (1 < n, m ≤ 300000), 
    where:
    - n is the position the frog wants to reach.
    - m is the number of leaves that will fall.
  - The second line contains m integers a0, a1, ..., a_(m-1) 
    (1 < ai < n), where ai represents the position where the i-th 
    leaf falls.

  Output:
  - The output should be a single integer:
    - The minimum number of leaves that need to fall for the frog 
      to safely jump across the river.
    - If the frog cannot cross, print `-1`.

  Example Input:
  5 8
  1 3 1 4 2 3 5 4

  Example Output:
  7
"""

def frog_set(n, m, leaves):
    positions = set()
    
    for i in range(m):
        positions.add(leaves[i]) 
        if len(positions) == n: 
            return i + 1

    return -1

def frog_dict(n, m, leaves):
    positions = {}
    
    for i in range(m):
        positions[leaves[i]] = True
        if len(positions) == n:
            return i + 1

    return -1 

n = int(input())
m = int(input())
leaves = list(map(int, input().split(' ')))
print(frog_set(n, m, leaves))
#print(frog_dict(n, m, leaves))


'''
n, m = 5, 8
leaves = [1, 3, 1, 4, 2, 3, 5, 4]
#print(frog_set(n, m, leaves))
print(frog_dict(n, m, leaves))
'''