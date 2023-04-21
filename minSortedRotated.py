def findMin(nums):
    l, r = 0, len(nums) - 1
    minimum = nums[0]

    while l <= r:
        mid = (l + r) // 2
        minimum = min(minimum, nums[mid])
        if nums[r] > nums[mid]:
            r = mid - 1
        else:
            l = mid + 1

    return minimum


print(findMin([8, 9, 1, 2, 3, 4, 5, 6, 7]))
