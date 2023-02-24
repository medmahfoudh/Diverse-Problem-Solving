def longest_increasing_subsequence_length(numbers):
    n = len(numbers)
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if numbers[j] < numbers[i]:
                dp[i] = max(dp[i], dp[j]+1)
    
    return max(dp)

# Example 
numbers = [10, 9, 2, 5, 3, 7, 101, 18]
result = longest_increasing_subsequence_length(numbers)
print(result)  # Output: 4
