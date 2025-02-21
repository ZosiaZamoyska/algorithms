'''
    A boy is doing his math homework.
    The task with a star contains a sequence of n integers.
    Boy's task is to circle exactly three numbers from this sequence in such a way that the sum of the elements between the circled ones is as large as possible.
    More precisely, if he circles the numbers from position a<b<c, we add a+1, a+2…, b-1 and b+1, b+2, … c-1.
    The boy is not very good at this task, so he called you.
    Help him and give the maximum sum that he can get from the given sequence of numbers.

    3 <= n <= 300,000
    -1,000,000 <= w0, w1, … <= 1,000,000

    Example:
    7
    3 2 6 -1 4 5 1

    Answer: 17
'''
def max_sum_n(n, arr):
    w = [0] * (n+1)
    for i in range(n-1, -1, -1):
        w[i] = max(w[i+1]+arr[i], arr[i])
    return w[:-1]

def between_sum(n, arr):
    pref = max_sum_n(n-2, arr[1:n-1])
    suf = list(reversed(max_sum_n(n-2, list(reversed(arr[1:n-1])))))
    ans = 0
    for i in range(1, n-3):
        sum = suf[i-1] + pref[i+1]
        ans = max(ans, sum)
    return ans
    
    
n = 7
arr = [3, 2, 6, -1, 4, 5, 1]
print(between_sum(n, arr))