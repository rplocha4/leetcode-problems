def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False
    s1_count = [0] * 26
    s2_count = [0] * 26
    matches = 0

    for i in range(len(s1)):
        s1_count[ord(s1[i]) - ord("a")] += 1
        s2_count[ord(s2[i]) - ord("a")] += 1

    for i in range(26):
        if s1_count[i] == s2_count[i]:
            matches += 1

    l = 0
    for r in range(len(s1), len(s2)):
        if matches == 26:
            return True

        ind = ord(s2[r]) - ord("a")

        s2_count[ind] += 1

        if s2_count[ind] == s1_count[ind]:
            matches += 1
        elif s2_count[ind] - 1 == s1_count[ind]:
            matches -= 1

        ind = ord(s2[l]) - ord("a")
        s2_count[ind] -= 1

        if s2_count[ind] == s1_count[ind]:
            matches += 1
        elif s2_count[ind] + 1 == s1_count[ind]:
            matches -= 1
        l += 1

    return matches == 26


print(checkInclusion("ab", "eidbaooo"))
