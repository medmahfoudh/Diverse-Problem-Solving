def longest_palindromic_subsequence(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = 1
    
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    
    i, j = 0, n-1
    result = ''
    while i <= j:
        if s[i] == s[j]:
            result += s[i]
            i += 1
            j -= 1
        elif dp[i+1][j] > dp[i][j-1]:
            i += 1
        else:
            j -= 1
    
    return result

# Example 
s = "babad"
result = longest_palindromic_subsequence(s)
print(result)  # Output: "bab"
