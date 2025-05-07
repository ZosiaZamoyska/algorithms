'''
    Given a string s, find the minimum number of operations required to make the string in a format of X+X.

    Allowed operations include:
    1. Deleting a letter from s
    2. Adding a letter to s
    3. Replacing a letter in s

    For example, "XYXX" -> requires 1 operation. 
    "ABCXYZDEFABCDEF" -> requires 3 operaitons.

    Answer t different test cases.
'''

def edit_distance(s1, s2):
    dp = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]
    for i in range(len(s1)+1):
        for j in range(len(s2)+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j],  
                                   dp[i][j-1],
                                   dp[i-1][j-1])

    return dp[len(s1)][len(s2)]


def solve():
    s = input()
    ans = len(s)
    if (ans > 1):
        for i in range(len(s)):
            x = s[:i]
            y = s[i:]
            ans = min(ans, edit_distance(x, y))
    print(ans)
    

t = int(input())

for i in range(t):
    solve()
