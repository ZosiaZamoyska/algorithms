'''
    Count Vowels

    Given a string and multiple queries [a, b], count the number of vowels in the substring from index a to b.
'''
def count_vowels(s, queries):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    n = len(s)
    prefix_vowels = [0] * (n + 1)
    
    for i in range(n):
        prefix_vowels[i + 1] = prefix_vowels[i] + (1 if s[i] in vowels else 0)
    
    return [prefix_vowels[b + 1] - prefix_vowels[a] for a, b in queries]

word = input()
m = int(input())
queries = []
for i in range(m):
    queries.append((map(int, input().split(' '))))

# word = "advbai"
# m = 3
# queries = [(0, 2), (1, 3), (2, 5)]
# Output: [1, 0, 2]

print(count_vowels(word, queries))  
