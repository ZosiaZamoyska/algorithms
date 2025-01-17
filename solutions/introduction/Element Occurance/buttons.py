'''
    We have n counters and m button presses. Initially, all counters are set to 0.
    Pressing any button i (from 1 to n) increments the value of the corresponding counter.
    The last button (n+1) sets all counters to the maximum value currently on any of them.
    We need to print the final values of the counters after m button presses.

    Input Format:
    - The first line contains two integers, n and m (1 ≤ n, m ≤ 1,000,000), where n is the number of counters and m is the number of presses.
    - The second line contains m integers P0, P1, ..., Pm-1 (1 ≤ Pi ≤ n+1), representing the sequence of button presses.

    Output Format:
    - Output n integers, representing the final values of the counters.

    Example Input:
    5 7 
    3 4 4 6 1 4 4 

    Example Output:
    3 2 2 4 2

'''

def process_buttons_optimized(n, m, presses):
    counters = [0] * n
    max_curr = 0
    max_count = 0

    for press in presses:
        if press == n + 1:
            max_count = max_curr
        else:
            if counters[press - 1] < max_count:
                counters[press - 1] = max_count

            counters[press - 1] += 1

            max_curr = max(max_curr, counters[press - 1])

    for i in range(n):
        counters[i] = max(counters[i], max_count)

    return counters

n, m = map(int, input().split())
presses = list(map(int, input().split()))

result = process_buttons_optimized(n, m, presses)

print(" ".join(map(str, result)))
