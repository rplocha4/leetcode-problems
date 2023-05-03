def pivotIndex(nums):
    sum_all = sum(nums)

    sum_left = 0

    for i, num in enumerate(nums):
        sum_right = sum_all - num - sum_left
        if sum_right == sum_left:
            return i
        sum_left += num

    return -1
