def longest_common_subsequence(str1, str2):
    m = len(str1)
    n = len(str2)

    memo = [[0 for j in range(n+1)] for i in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                memo[i][j] = memo[i-1][j-1] + 1
            else:
                memo[i][j] = max(memo[i-1][j], memo[i][j-1])
   
    return memo[m][n]
