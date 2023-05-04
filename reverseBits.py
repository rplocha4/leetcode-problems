def reverseBits(n):
    res = 0

    for _ in range(32):
        res <<= 1
        if n & 1 == 1:
            res += 1
        n >>= 1
    return res