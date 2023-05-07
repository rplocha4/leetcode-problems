def containsNearbyDuplicate(nums, k):
    window = set()

    l, r = 0, 0
    while r <= len(nums) - 1:
        if r - l > k:
            window.remove(nums[l])
            l += 1
        if nums[r] in window:
            return True
        window.add(nums[r])
        r += 1

    return False
