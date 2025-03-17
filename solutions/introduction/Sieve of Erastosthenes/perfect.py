# Recall that a **perfect number** is a natural number greater than 1 that is equal to the sum of all its proper divisors. 
# A **second-kind perfect number** is a natural number greater than 1 that is equal to the product of all its proper divisors.
# 
# For example, proper divisors of 27 are 1, 3, and 9, and since 1 * 3 * 9 = 27, 27 is a second-kind perfect number.
# A proper divisor of a number is a natural divisor other than the number itself.
#
# We would like to know **how many second-kind perfect numbers are contained in certain ranges**.
#
# Input:
# First line: integer t - number of ranges.
# Next t lines: two integers a and b - range boundaries (inclusive).
#
# Output:
# For each range, output a single integer - number of second-kind perfect numbers in that range.
#
# Example:
#
# 2
# 27 30
# 2 10
#
# Answer:
# 1
# 3
#


MAX = 10**6 + 1

F = [0] * MAX
pref = [0] * MAX

def sieve():
    for i in range(2, int(MAX ** 0.5) + 1):
        if F[i] == 0:
            for j in range(i * i, MAX, i):
                if F[j] == 0:
                    F[j] = i
    for i in range(2, MAX):
        if F[i] == 0:
            F[i] = i

def preprocess():
    for i in range(2, int(MAX ** (1/3)) + 2):
        if F[i] == i:
            cube = i * i * i
            if cube < MAX:
                pref[cube] = 1

    for i in range(2, MAX):
        if F[i] != 0 and F[i // F[i]] == (i // F[i]) and F[i] != i // F[i]:
            pref[i] = 1

    for i in range(1, MAX):
        pref[i] += pref[i - 1]

def count_second_sort_perfect(a, b):
    return pref[b] - pref[a - 1] if a > 1 else pref[b]

sieve()
preprocess()

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(count_second_sort_perfect(a, b))