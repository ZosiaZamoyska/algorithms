
'''
    Youngest Hamster in Range

    Given a list of n integers (1 <= n <= 500,000), where each value represents the age of a hamster (1 to 5).
    There are m queries, each specifying a range [a, b]. For each query, return the youngest hamster in that range.
'''
def youngest_hamster(ages, queries):
    n = len(ages)
    
    prefix_counts = [[0] * (n + 1) for _ in range(6)]
    
    for i in range(n):
        for age in range(1, 6):
            prefix_counts[age][i + 1] = prefix_counts[age][i] + (1 if ages[i] == age else 0)
    
    results = []
    for a, b in queries:
        for age in range(1, 6):
            if prefix_counts[age][b] - prefix_counts[age][a - 1] > 0:
                results.append(str(age))
                break
    
    print(*results, sep='\n')

n, m = map(int, input().split(' '))

ages = list(map(int, input().split(' ')))
queries = []
for i in range(m):
    queries.append((map(int, input().split(' '))))

#n, m = 5, 3
#ages = [2, 3, 4, 3, 1]
#queries = [(1, 3), (2, 5), (2, 4)]

youngest_hamster(ages, queries)