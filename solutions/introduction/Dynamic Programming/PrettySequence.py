'''
A boy is constructing sequences made of integers in the range from 0 to k.
He considers a sequence "nice" if the absolute difference between any two
adjacent elements is at most 1.

We want to find out how many different nice sequences of each given length
can be formed. Two sequences are considered different if they differ at
any position.

Your task is to calculate, for each given sequence length, the number of such
nice sequences, modulo q.

Input:
- First line contains three integers: m, k, q
  where m is the number of queries (lengths of sequences to check),
  k is the maximum integer value in the sequence,
  and q is the modulo value.

- Second line contains m integers: n₁, n₂, ..., nₘ
  where each nᵢ is a length of sequence to evaluate.

Output:
- For each length nᵢ, print the number of nice sequences of length nᵢ modulo q.

Example:
Input:
3 1 10
1 2 3

Output:
2 4 8
'''

def count_nice_sequences(lengths, k, q):
    max_n = max(lengths)
    
    dp = [[0] * (k + 1) for _ in range(max_n + 1)]

    for j in range(k + 1):
        dp[1][j] = 1

    for i in range(2, max_n + 1):
        for j in range(k + 1):
            dp[i][j] = dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i - 1][j - 1]
            if j < k:
                dp[i][j] += dp[i - 1][j + 1]
            dp[i][j] %= q

    results = []
    for n in lengths:
        total = sum(dp[n][j] for j in range(k + 1)) % q
        results.append(total)

    return results

m, k, q = map(int, input().split())
lengths = list(map(int, input().split()))

results = count_nice_sequences(lengths, k, q)
print(" ".join(map(str, results)))
