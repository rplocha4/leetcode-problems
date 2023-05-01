def validPalindrome(s):
    l, r = 0, len(s) - 1

    def validPalindromeRemovedChar(s, l, r):
        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True

    while l <= r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            return validPalindromeRemovedChar(
                s, l + 1, r
            ) or validPalindromeRemovedChar(s, l, r - 1)
    return True
