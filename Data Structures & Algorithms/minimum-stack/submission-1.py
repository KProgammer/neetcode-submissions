from sortedcontainers import SortedList
class MinStack:

    def __init__(self):
        self.stack = []
        # self.order = SortedList([])

    def push(self, val: int) -> None:
        min_val = val
        if (self.stack) and (self.stack[-1][1] < min_val):
            min_val = self.stack[-1][1]
        self.stack.append(tuple([val,min_val]))

    def pop(self) -> None:
        # self.order.discard(self.stack[-1])
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        # return self.order[0]
        return self.stack[-1][1]
    
    # min heap which can insert in log n time, but that will be too much to do
