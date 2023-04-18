def searchMatrix(matrix, target):

    f, l = 0, len(matrix) - 1
    row = []
    while f <= l:
        mid = (f + l) // 2
        if matrix[mid][0] <= target and matrix[mid][-1] >= target:
            row = matrix[mid]
            break
        if matrix[mid][0] > target:
            l = mid - 1
        else:
            f = mid + 1

    l, r = 0, len(row) - 1
    while l <= r:
        mid = (l + r) // 2
        if row[mid] == target:
            return True
        if row[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return False
