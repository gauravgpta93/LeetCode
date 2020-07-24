import heapq


class DinnerPlates:

    def __init__(self, capacity: int):
        self._stacks = list()
        self._partial = list()
        self._capacity = capacity

    def push(self, val: int) -> None:
        while self._partial and self._partial[0] < len(self._stacks) and len(
                self._stacks[self._partial[0]]) == self._capacity:
            heapq.heappop(self._partial)
        if not self._partial:
            heapq.heappush(self._partial, len(self._stacks))
        if self._partial[0] == len(self._stacks):
            self._stacks.append(list())
        self._stacks[self._partial[0]].append(val)

    def pop(self) -> int:
        while self._stacks and not self._stacks[-1]:
            self._stacks.pop()
        return self.popAtStack(len(self._stacks) - 1)

    def popAtStack(self, index: int) -> int:
        if 0 <= index < len(self._stacks) and self._stacks[index]:
            heapq.heappush(self._partial, index)
            return self._stacks[index].pop()
        return -1
# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)
