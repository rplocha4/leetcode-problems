def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if seen.get(target - num) is not None:
            return [seen[target - num], i]
        seen[num] = i