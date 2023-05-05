def countingBits(n):
    dp = [0] * (n + 1)
    offset = 1
    for i in range(1, n + 1):
        dp[i] = dp[i - offset] + 1
        if i + 1 == offset * 2:
            offset *= 2
    return dp


print(countingBits(5))
