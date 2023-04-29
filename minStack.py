class MinStack(object):
    def __init__(self):
        self.stack = []
        self.m = []

    def push(self, val):
        self.stack.append(val)
        if not self.m:
            self.m.append(val)
        elif val < self.m[-1]:
            self.m.append(val)
        else:
            self.m.append(self.m[-1])

    def pop(self):
        self.stack.pop()
        self.m.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):

        return self.m[-1]
