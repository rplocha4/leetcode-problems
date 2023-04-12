def productExceptSelf(nums):
    prefix = 1
    suffix = 1
    result = []
    for i in range(len(nums)):
        result.append(prefix)
        prefix *= nums[i]
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    return result

print(productExceptSelf([1, 2, 3, 4]))