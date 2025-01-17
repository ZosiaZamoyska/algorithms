"""
    We are given an integer m (1 < m ≤ 1,000,000) and two arrays, A and B, 
    each containing n integers: 
    A = [a0, a1, ..., an-1] and B = [b0, b1, ..., bn-1], 
    where 0 < ai, bi < m.

    We need to determine whether there exists a swap operation that can be 
    performed on these arrays such that, after the swap, the sum of elements 
    in array A is equal to the sum of elements in array B.

    A "swap operation" means selecting one element from array A and one element 
    from array B and exchanging their values.
"""

def find_swap(A, B):
    sumA = sum(A)
    sumB = sum(B)

    diff = sumA - sumB
    setB = set(B)

    if diff % 2 != 0:
        return False
    
    # for each element a in A, we are looking if there exists a b in B such that
    # a = b + diff / 2
    for a in A:
        if (a - diff // 2) in setB:
            return True
    return False

A = list(map(int, input().split(' '))) # A = [1, 2, 5, 8]
B = list(map(int, input().split(' '))) # B = [3, 6, 4, 7]

print(find_swap(A, B))