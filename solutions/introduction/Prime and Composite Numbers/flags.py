'''
    A boy is packing for an expedition to the Mountains. 
    He already has a map of the route he will follow. 
    These are n consecutive places located at certain heights. 
    A peak is a place for which two neighboring places are lower. 
    We assume that the first and last place are not peaks. 
    The boy wants to place flags on the peaks. 
    He decides that if he takes k flags with him, then the distance between any two flags must be at least k. 
    Places x < y are exactly y-x apart. 
    Help the boy and calculate the maximum number of flags he can place. 
    We know that the boy has an unlimited number of flags that he can take on his expedition.

    Example
    10
    3 5 2 1 4 3 6 1 7 2 

    Answer
    3

    Flags can be placed at (1, 4, 8).    
'''

def max_flags(t):
    n = len(t)
    if n < 3:
        return 0 

    peaks = [0] * n
    peak_indices = []
    
    for i in range(1, n - 1):
        if t[i] > t[i - 1] and t[i] > t[i + 1]:
            peaks[i] = 1
            peak_indices.append(i)

    if not peak_indices:
        return 0

    next_peak = [-1] * n
    last_peak = -1
    
    for i in range(n - 1, -1, -1):
        if peaks[i] == 1:
            last_peak = i
        next_peak[i] = last_peak

    max_flags = 0
    limit = int(n**0.5 + 1)
    
    for k in range(1, limit + 1):
        pos = 0
        count = 0
        
        while pos < n and count < k:
            pos = next_peak[pos]
            if pos == -1:
                break
            count += 1
            pos += k 
        max_flags = max(max_flags, count)

    return max_flags


t = [3, 5, 2, 1, 4, 3, 6, 1, 7, 2]
print(max_flags(t))