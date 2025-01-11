"""
  Bytek wrote down n numbers on a piece of paper. He is now wondering whether 
  they form a permutation of numbers from 1 to n, meaning that each number 
  from the set {1, 2, ..., n} appears exactly once in the sequence.

  Input:
  - The first line of input contains a single integer n (1 < n ≤ 1,000,000), 
    representing the number of numbers Bytek wrote down.
  - The second line contains a sequence of n integers a0, a1, …, a_(n-1) 
    (1 ≤ ai ≤ 10^9), where ai represents the i-th number in Bytek's sequence.

  Output:
  - The output should contain a single word:
    - "YES" if the sequence is a permutation of numbers from 1 to n.
    - "NO" otherwise.

  Example Input:
  5
  1 4 3 2 5

  Example Output:
  YES

  Example Input:
  5
  1 4 3 3 5

  Example Output:
  NO
"""

def is_permutation(n, numbers):
    if set(numbers) == set(range(1, n + 1)):
        return "YES"
    return "NO"

n = int(input())
numbers = list(map(int, input().split(' ')))
print(is_permutation(n, numbers))

'''
# Example Inputs

n = 5
numbers = [1, 4, 3, 2, 5]
print(is_permutation(n, numbers))

numbers = [1, 4, 3, 3, 5]
print(is_permutation(n, numbers))
'''
