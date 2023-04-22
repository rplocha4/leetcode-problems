def lengthOfLongestSubstring(s):
    if len(s) < 2:
        return len(s)
    max_len = 0
    l, r = 0, 1
    duplicates = set(s[l])
    while r < len(s):
        while s[r] in duplicates:
            duplicates.remove(s[l])
            l += 1
        duplicates.add(s[r])
        r += 1
        max_len = max(max_len, r - l)
    return max_len


print(lengthOfLongestSubstring("bbbb"))
