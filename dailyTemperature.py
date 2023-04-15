def dailyTemperatures(temperatures):
    stack = []
    res = [0] * len(temperatures)

    for i, num in enumerate(temperatures):
        while stack and num > stack[-1][0]:
            val = stack.pop()
            res[val[1]] = i - val[1]
        stack.append([num, i])

    return res


print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
