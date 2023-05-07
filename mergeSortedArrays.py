def merge(nums1, m, nums2, n):
    p1, p2 = m - 1, n - 1
    last = -1

    for i in range(len(nums1) - 1, -1, -1):
        if p1 < 0 or p2 < 0:
            last = i
            break
        if nums1[p1] >= nums2[p2]:
            nums1[i] = nums1[p1]
            nums1[p1] = 0
            p1 -= 1
        else:
            nums1[i] = nums2[p2]
            p2 -= 1

    if last != -1:
        while p2 >= 0:
            nums1[last] = nums2[p2]
            p2 -= 1
            last -= 1
