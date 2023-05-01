def getConcatenation(nums):
    res = [0] * 2 * len(nums)

    for i, num in enumerate(nums):
        res[i] = num
        res[i + len(nums)] = num
    return res
