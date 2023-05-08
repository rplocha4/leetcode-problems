def generate(numRow):
    res = []

    for i in range(numRows):
        row = [1] * (i + 1)
        for j in range(i):
            if j != 0 and j != len(row) - 1:
                row[j] = res[i - 1][j - 1] + res[i - 1][j]
        res.append(row)
    return res
