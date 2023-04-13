def trap(height):
    if len(height) < 3:
        return 0

    l, r = 0, len(height) - 1
    l_max, r_max = height[l], height[r]
    total = 0

    while l < r:
        l_max = max(l_max, height[l])
        r_max = max(r_max, height[r])
        if l_max < r_max:
            total += l_max - height[l]
            l += 1
        else:
            total += r_max - height[r]
            r -= 1
    
    return total