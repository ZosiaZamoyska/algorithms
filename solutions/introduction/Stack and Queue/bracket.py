"""
A non-uniform bracket sequence is any permutation of opening and closing brackets: 
- round (), 
- square [], 
- curly {}.

A bracket sequence is correct if it can be completed with numbers and operations 
such that the mathematical expression is valid.

Example:
- "{[()()]}" is correct.
- "([)()]" is incorrect.

Task: Determine whether each input bracket sequence is correct.

Input:
- N (1 ≤ N ≤ 1000) — the number of bracket sequences to check.
- N sequences, each of length between 1 and 250 characters.

Output:
- Print "YES" if the sequence is correct, otherwise print "NO".

Example:
Input:
2
{[()()]}
([)()]

Output:
YES
NO
"""

def is_valid_bracket_sequence(s):
    bracket_map = {'(': ')', '[': ']', '{': '}'}
    stack = []

    for char in s:
        if char in bracket_map:
            stack.append(char)
        else:
            if not stack or bracket_map[stack.pop()] != char:
                return "NO"

    return "YES" if not stack else "NO"

n = int(input())
for _ in range(n):
    sequence = input().strip()
    print(is_valid_bracket_sequence(sequence))
