import math


def reverseInteger(x):
    min = -(2**31)
    max = 2**31 - 1
    res = 0

    while x:
        digit = int(math.fmod(x, 10))
        x = int(x / 10)
        if res > max // 10 or (res == max // 10 and digit >= max & 10):
            return 0

        if res < min // 10 or (res == min // 10 and digit <= min % 10):
            return 0
        res = res * 10 + digit
    return res


print(reverseInteger(123))
print(reverseInteger(-123))
print(reverseInteger(-1232131321312123))
