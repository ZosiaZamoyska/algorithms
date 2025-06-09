'''
You are given a string 𝑠 consisting of lowercase Latin letters.

You can perform the following operation with the string 𝑠: choose a contiguous substring (possibly empty) of 𝑠 and shuffle it (reorder the characters in the substring as you wish).

Recall that a palindrome is a string that reads the same way from the first character to the last and from the last character to the first. For example, the strings a, bab, acca, bcabcbacb are palindromes, but the strings ab, abbbaa, cccb are not.

Your task is to determine the minimum possible length of the substring on which the aforementioned operation must be performed in order to convert the given string 𝑠 into a palindrome.
    https://codeforces.com/problemset/problem/2069/D
'''

def solve():
    t = int(input())
    
    for _ in range(t):
        s = input().strip()
        n = len(s)
        
        i = 0
        while i < n // 2 and s[i] == s[n - i - 1]:
            i += 1
        
        n -= 2 * i
        s = s[i:i + n]
        
        ans = n
        
        for _ in range(2):
            left, right = 0, n
            
            while left <= right:
                mid = (left + right) // 2
                
                char_count = [0] * 26
                for j in range(mid):
                    char_count[ord(s[j]) - ord('a')] += 1
                
                valid = True
                
                for j in range(min(n // 2, n - mid)):
                    required_char = s[n - j - 1]
                    
                    if j < mid:
                        if char_count[ord(required_char) - ord('a')] > 0:
                            char_count[ord(required_char) - ord('a')] -= 1
                        else:
                            valid = False
                            break
                    else:
                        if required_char != s[j]:
                            valid = False
                            break
                
                if valid:
                    for count in char_count:
                        if count % 2 != 0:
                            valid = False
                            break
                
                if valid:
                    right = mid - 1
                else:
                    left = mid + 1
            
            ans = min(ans, right + 1)
            
            s = s[::-1]
        
        print(ans)

solve()