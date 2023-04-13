def longestConsecutive(nums):
    if len(nums) == 0:
        return 0
    nums_set = set(nums)
    longest = 0
    for num in nums:
        curr_len = 0
        if num + 1 in nums_set:
            continue
        curr_num = num
        while curr_num in nums_set:
            curr_len += 1
            curr_num -= 1
        longest = max(longest, curr_len)

    return longest
