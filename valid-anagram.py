def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    seen = {}
    for char in s:
        if seen.get(char):
            seen[char] += 1
        else:
            seen[char] = 1
    for char in t:
        if seen.get(char):
            seen[char] -= 1
        else:
            return False
    for char in seen:
        if seen[char] != 0:
            return False
    return True    