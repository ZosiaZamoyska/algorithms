#
# A boy collects tangerines into two baskets with capacity up to 'n'. His reward is GCD(x, y) + LCM(x, y).
# Goal: Find x, y ≤ n to maximize the reward.
#
# Example:
# 3
# Answer:
# 7
# 

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

def max_reward(n):
    if n == 2:
        x, y = 2, 2
    else:
        x, y = n, n - 1
    
    reward = gcd(x, y) + lcm(x, y)
    return reward

n = int(input())
print(max_reward(n))
