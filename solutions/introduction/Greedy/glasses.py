'''
A girl lined up a number of glasses and poured the same amount of water into each one.
Then she left the room. During her absence, a boy came in and decided to play a prank
by quickly pouring water between the glasses, making the water levels uneven.

When the girl returned and saw the uneven water distribution, she got upset and ran to her mother.
An investigation could not find the culprit, so now the only thing to do is to redistribute the water
such that each glass ends up with the same amount of water.

Given the current amount of water in each glass, determine whether it's possible to make all glasses
contain the same amount, and if so, compute the minimum number of water transfer operations needed.
A transfer consists of pouring water from one glass to another.
'''

def min_transfers(glasses):
    n = len(glasses)
    total = sum(glasses)
    
    if total % n != 0:
        return -1

    target = total // n
    prefix_sum = [0] * (n + 1)
    result = 0

    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + glasses[i]

    for i in range(1, n):
        if prefix_sum[i] != i * target:
            result += 1

    return result

glasses = list(map(int, input().split()))
res = min_transfers(glasses)

if res == -1:
    print(-1)
else:
    print(res)
