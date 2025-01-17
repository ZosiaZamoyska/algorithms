'''
    Given a list of n integers (1 <= n <= 1,000,000), where each value represents the direction of a car (0 = east, 1 = west).
    Count how many pairs of passing cars exist (cars traveling in opposite directions meeting at the same point).
'''

def count_passing_cars(s):
    east = 0
    passing_pairs = 0
    
    for car in s:
        if car == 0:
            east += 1
        else:
            passing_pairs += east
        
    return passing_pairs

s = list(map(int, input().split(' ')))
#s = [0, 1, 0, 1, 1]
print(count_passing_cars(s))
