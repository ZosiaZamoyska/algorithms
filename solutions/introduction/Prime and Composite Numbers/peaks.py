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
    
    for segment_length in get_divisors(n):
        count = 0
        last_flag = -segment_length
        valid_segments = [False] * (n // segment_length)
        
        for i in range(1, n-1):
            if heights[i - 1] < heights[i] > heights[i + 1]:
                valid_segments[i // segment_length] = True
        if sum(valid_segments) ==  n // segment_length:
            return n // segment_length

    return -1

n = int(input())
heights = list(map(int, input().split(' ')))

#n = 12
#heights = [1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]

print(max_flags(heights))
