from sortedcontainers import SortedList
class MinStack:

    def __init__(self):
        self.stack = []
        self.order = SortedList([])
        self.min_value = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.order.add(val)

    def pop(self) -> None:
        self.order.discard(self.stack[-1])
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.order[0]
    
    # min heap which can insert in log n time, but that will be too much to do
