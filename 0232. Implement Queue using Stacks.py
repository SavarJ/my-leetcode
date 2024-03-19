class MyQueue:
    def __init__(self):
        self.a, self.b = [], []

    def push(self, x: int) -> None:
        self.a.append(x)

    def pop(self) -> int:
        return [self.peek(), self.b.pop()][1]

    def peek(self) -> int:
        if self.b: return self.b[-1]
        while self.a:
            self.b.append(self.a.pop())
        return self.b[-1]

    def empty(self) -> bool:
        return not self.a and not self.b
