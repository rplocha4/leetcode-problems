def moveZeroes( nums):

    if len(nums) < 2: return

    l, r = 0, 1
    while r < len(nums):
        if nums[l] == 0 and nums[r]!=0:
            nums[l], nums[r] = nums[r], nums[l]
        
        if nums[l]!=0:
            l+=1
        r+=1
        