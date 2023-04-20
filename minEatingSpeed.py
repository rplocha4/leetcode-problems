import math


def minEatingSpeed(piles, h):
    def canFinish(piles, h, speed):
        return sum(math.ceil(pile / speed) for pile in piles) <= h

    l, r = 1, max(piles)
    while l < r:
        m = (l + r) // 2
        if not canFinish(piles, h, m):
            l = m + 1
        else:
            r = m
    return l


print(minEatingSpeed([3, 6, 7, 11], 8))
