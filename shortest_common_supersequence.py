def shortest_common_supersequence(s1, s2):
    m, n = len(s1), len(s2)

    memo = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                memo[i][j] = 1 + memo[i-1][j-1]
            else:
                memo[i][j] = 1 + min(memo[i-1][j], memo[i][j-1])
    # Return the length of the shortest common supersequence
    return memo[m][n]
