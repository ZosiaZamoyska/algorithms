'''
    A boy is packing for an expedition to the Mountains. 
    He already has a map of the route he will follow. 
    These are n consecutive places located at certain heights. 
    A peak is a place for which two neighboring places are lower. 
    We assume that the first and last place are not peaks. 
    The boy would like to divide the entire route into coherent sections with the same number of places. 
    In each section, he would like to place exactly one flag. 
    He decided that he can mix up the flags only on the peaks. 
    Help the boy and calculate the maximum number of flags he can place. 

    Example 
    12 
    1 5 3 4 3 4 1 2 3 4 6 2 
    Answer 
    3 

    The boy divided the route into three sections of length 4. 
    He can now place flags on peaks (3, 5, 10) or (1, 5, 10)
'''
def get_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5 + 1)):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sorted(divisors)

def max_flags(heights):
    n = len(heights)
    max_flags = 0
    divisors = get_divisors(n)

    for length in divisors:
        seg = n // length
        segments = [False] * seg
    
        for i in range(1, n-1):
            if heights[i] > heights[i-1] and heights[i] > heights[i+1]:
                segments[ i // length ] = True
        if sum(segments) == seg:
            max_flags = max(max_flags, seg)
    
    return max_flags

n = int(input())
heights = list(map(int, input().split(' ')))

#n = 12
#heights = [1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]

print(max_flags(heights))
