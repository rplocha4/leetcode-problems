def missingNumber(nums):
    res = 0

    for num in nums:
        res ^=num
    for i in range(len(nums) + 1):
        res ^= i
    return res