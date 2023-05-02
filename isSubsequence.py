def isSubsequence(s, t):
    if not s:
        return True

    s_p = 0
    t_p = 0

    while t_p < len(t):
        if t[t_p] == s[s_p]:
            s_p += 1
            if s_p == len(s):
                return True
        t_p += 1
    return False
