# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):


def guessNumber(n):
    l, r = 1, n

    while l <= r:
        m = (l + r) // 2
        guess_res = guess(m)
        if guess_res == 0:
            return m
        elif guess_res == -1:
            r = m - 1
        else:
            l = m + 1
