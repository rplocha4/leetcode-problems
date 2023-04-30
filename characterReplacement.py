def characterReplacement(s, k):
    left = 0
    s_map = {}

    res = 0

    for right in range(len(s)):
        s_map[s[right]] = 1 + s_map.get(s[right], 0)

        while right - left + 1 - max(s_map.values()) > k:
            s_map[s[left]] -= 1
            left += 1

        res = max(right - left + 1, res)
    return res
