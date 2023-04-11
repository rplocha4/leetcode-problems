# def containsDuplicate(self, nums: List[int]) -> bool:
#     return len(nums) != len(set(nums))


def containsDuplicate(self, nums: List[int]) -> bool:
    seen = {}
    for num in nums:
        if seen.get(num):
            return True
        seen[num] = 1
    return False
