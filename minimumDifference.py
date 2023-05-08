def minimumDifference(nums, k):
    nums.sort()
    min_res = float("inf")
    l, r = 0, k - 1
    while r < len(nums):
        min_res = min(min_res, nums[r] - nums[l])
        r += 1
        l += 1
    return min_res
