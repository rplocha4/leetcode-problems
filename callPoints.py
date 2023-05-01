def callPoints(operations):
    s = []
    for char in operations:
        if char == "+":
            s.append(s[-1] + s[-2])
        elif char == "D":
            s.append(2 * s[-1])
        elif char == "C":
            s.pop()
        else:
            s.append(int(char))
    return sum(s)
