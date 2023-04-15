def largestRectangleArea(heights):

    stack = []
    max_area = 0

    for i, height in enumerate(heights):
        start = i

        while stack and height < stack[-1][1]:
            indx, h = stack.pop()
            max_area = max(max_area, (i - indx) * h)
            start = indx

        stack.append([start, height])
    for i, h in stack:
        max_area = max(max_area, (len(heights) - i) * h)
    return max_area


print(largestRectangleArea([2, 1, 2]))
