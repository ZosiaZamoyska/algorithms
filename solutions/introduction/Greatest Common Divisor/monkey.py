# 
# A cheerful monkey found a new game. She arranged n cages with animals (each cage contains exactly one animal) in a circle 
# and jumps over them. The monkey always jumps over d consecutive cages and always opens the one she lands on. 
# She stops when she jumps on a cage that has already been opened. 
# Your task is to determine how many animals will be released. 
# Initially, all cages are closed, and each animal (other than the monkey) will leave when its cage is opened.
#
# Input: Two integers n (number of cages) and d (jump size)
# Output: Number of released animals (unique cages visited)
#
# Example:
# Input:
# 3 1
# Output:
# 3
#
# Input:
# 3 2
# Output:
# 3
#

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

def released_animals(n, d):
    return n // gcd(n, d)

t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    print(released_animals(n, d))
