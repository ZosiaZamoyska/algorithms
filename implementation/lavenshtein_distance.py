def find_distance(s1, s2):
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
 
print(find_distance("ABCXYZDEFABCDEF", "ABCDEFABCDEF")) # 3