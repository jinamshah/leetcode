class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        self.currentSize = 0

    def push(self, x: int) -> None:
        if self.currentSize < self.maxSize:
            self.stack.append(x)
            self.currentSize += 1
    def pop(self) -> int:
        if self.currentSize > 0:
            lastElement = self.stack[-1]
            self.stack = self.stack[:-1]
            self.currentSize -= 1
            return lastElement
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        if self.currentSize >= k:
            self.stack[:k] = [val+x for x in self.stack[:k]]
        else:
            self.stack = [val+x for x in self.stack]
            print(self.stack)


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)