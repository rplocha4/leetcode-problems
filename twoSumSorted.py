def twoSumSorted(numbers, target):

    l, r = 0, len(numbers) - 1
    while l < r:
        if numbers[l] + numbers[r] == target:
            return [l + 1, r + 1]
        elif numbers[l] + numbers[r] > target:
            r -= 1
        else:
            l += 1
    return []


print(twoSumSorted([2, 7, 11, 15], 9))
