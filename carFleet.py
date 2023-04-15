def carFleet(target, position, speed):

    pos_speed = sorted(zip(position, speed))
    stack = []

    for pos, spd in reversed(pos_speed):
        time = (target - pos) / spd
        stack.append(time)
        if len(stack) > 1 and stack[-1] <= stack[-2]:
            stack.pop()

    return len(stack)


print(carFleet(10, [6, 8], [3, 2]))
