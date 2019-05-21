# 无论是采用两个栈，还是一个栈两个字段，都是以空间换时间实现o1
# 注意pop后，更新最小值需要考虑周全
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = float('inf')
        self.stack = []

    def push(self, x: int) -> None:
        if x < self.min:
            self.min = x
        self.stack.append((x, self.min))

    def pop(self) -> None:
        num, _ = self.stack.pop()
        #         更新最小值
        if not self.stack:
            self.min = float('inf')
        else:
            _, self.min = self.stack[-1]
        return num

    def top(self) -> int:
        tmp, _ = self.stack[-1]
        return tmp

    def getMin(self) -> int:
        _, tmp = self.stack[-1]
        return tmp

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()