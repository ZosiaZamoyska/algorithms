'''
    There are n coins, numbered from 1 to n, on the table and n people.
    Each person from 1 to n, flips certain coins.
    To be specific, i-th person flips coins numbered i, 2*i, 3*i, ..., etc.
    How many coins will be flipped at the end?
    
    Example 
    For 10 coins and 10 people, there will be 3 coins flipped: 1, 4, and 9.
'''

def coins_flipped_simulated(n):
    coins = [0] * (n+1)

    for i in range(1, n+1):
        k = i
        while k <= n:
            coins[k] = 1 - coins[k]
            k += i

    return sum(coins)

def coins_flipped(n):
    return int(n ** 0.5)

n = int(input())
print(coins_flipped_simulated(n))
