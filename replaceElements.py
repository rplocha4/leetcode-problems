def replaceElement(arr):
    greatest_so_far = -1
    res = [0] * len(arr)
    for i, num in enumerate(reversed(arr)):
        res[len(arr) - i - 1] = greatest_so_far
        greatest_so_far = max(greatest_so_far, num)
    return res
