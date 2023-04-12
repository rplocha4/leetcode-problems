# def containsDuplicate(nums):
#     return len(nums) != len(set(nums))


def containsDuplicate(nums):
    seen = {}
    for num in nums:
        if seen.get(num):
            return True
        seen[num] = 1
    return False
