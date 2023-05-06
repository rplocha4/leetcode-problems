def sumOfTwoIntegers(a, b):
    while b:
        a, b = a ^ b, (a & b) << 1
    return a

print(sumOfTwoIntegers(1, 2))