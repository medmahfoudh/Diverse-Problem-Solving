def max_subarray_sum(nums):
    n = len(nums)
    memo = [0] * n
    memo[0] = nums[0]
    max_sum = nums[0]

    for i in range(1, n):
        memo[i] = max(nums[i], nums[i] + memo[i-1])
        max_sum = max(max_sum, memo[i])
    return max_sum


