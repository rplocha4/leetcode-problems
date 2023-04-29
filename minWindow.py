def minWindow(s, t):
    s_map = {}
    t_map = {}
    left, right = 0, 0
    min_len = float("inf")
    res = ""
    for c in t:
        t_map[c] = 1 + t_map.get(c, 0)

    goal = len(t_map)
    have = 0

    while right < len(s):
        c = s[right]
        s_map[c] = 1 + s_map.get(c, 0)
        if c in t_map and s_map[c] == t_map[c]:
            have += 1
        while have == goal:
            sub_len = right - left + 1
            if sub_len < min_len:
                min_len = sub_len
                res = s[left : right + 1]
            s_map[s[left]] -= 1
            if s[left] in t_map and s_map[s[left]] < t_map[s[left]]:
                have -= 1

            left += 1
        right += 1
    return res
