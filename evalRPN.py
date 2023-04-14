def evalRPN(tokens):
    stack = []
    for char in tokens:
        if char in "+-*/":
            b = stack.pop()
            a = stack.pop()
            if char == "+":
                stack.append(a + b)
            elif char == "-":
                stack.append(a - b)
            elif char == "*":
                stack.append(a * b)
            elif char == "/":
                stack.append(int(a / b))
        else:
            stack.append(int(char))
    return stack.pop()


print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
