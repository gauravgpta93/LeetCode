class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._queue = list()

    def push(self, x: int) -> None:
        if not len(self._queue):
            self._queue.append((x, x))
        else:
            self._queue.append((x, min(x, self._get_current_lowest())))

    def pop(self) -> None:
        self._queue.pop()

    def top(self) -> int:
        return self._queue[-1][0]

    def getMin(self) -> int:
        return self._get_current_lowest()

    def _get_current_lowest(self):
        return self._queue[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()