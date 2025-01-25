'''
    We are given a sequence of n >= 0 integers a0, a1, a2, ..., a(n-1),
    where -2 * 10^9 <= ai <= 2 * 10^9. 
    The task is to calculate how many distinct numbers appear in this sequence.
'''
def count_distinct_numbers(sequence):
    if not sequence:
        return 0
    
    sorted_sequence = sorted(sequence)
    
    distinct_count = 1  
    
    for i in range(1, len(sorted_sequence)):
        if sorted_sequence[i] != sorted_sequence[i - 1]:
            distinct_count += 1
    
    return distinct_count

sequence = list(map(int, input().strip().split()))[:n]
#sequence = [3, 1, 2, 3, 2, 1, 4]
print(count_distinct_numbers(sequence))
