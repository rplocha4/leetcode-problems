def sortedSquares(nums):
    res = [0] * len(nums)
    p = len(nums) - 1
    l, r = 0, len(nums) - 1
    while l <= r:
        left = abs(nums[l])
        right = abs(nums[r])

        if left >= right:
            res[p] = left * left
            l += 1
        else:
            res[p] = right * right
            r -= 1
        p -= 1
    return res
