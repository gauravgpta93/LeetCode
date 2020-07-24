class DinnerPlates:

    def __init__(self, capacity: int):
        self._partial_empty = list()
        self._stacks_dict = dict()
        self._used = list()
        if capacity > 0:
            self._capacity = capacity

    def push(self, val: int) -> None:
        if not len(self._partial_empty):
            current_index = self._get_next_stack_index()
            self._partial_empty.append(current_index)
            self._stacks_dict[current_index] = [val]
        else:
            current_index = self._lowest_index()
            self._stacks_dict[current_index].append(val)
        self._clean_up(current_index)

    def pop(self) -> int:
        if not (len(self._used)):
            return -1
        current_index = self._used[-1]
        pop_value = self._stacks_dict[current_index].pop()
        self._pop_cleanup(current_index)
        return pop_value

    def popAtStack(self, index: int) -> int:
        index = index + 1
        if index not in self._stacks_dict or not len(self._stacks_dict[index]):
            return -1
        if index == self._used[-1]:
            return self.pop()
        if index not in self._partial_empty:
            self._partial_empty.append(index)
        self._partial_empty.sort()
        return self._stacks_dict[index].pop()

    def _get_next_stack_index(self):
        self._used.append(len(self._used) + 1)
        return self._used[-1]

    def _lowest_index(self):
        return self._partial_empty[0]

    def _clean_up(self, current_index):
        total_length = len(self._stacks_dict[current_index])
        if total_length == self._capacity:
            self._partial_empty.pop(0)

    def _pop_cleanup(self, current_index):
        stack_size = len(self._stacks_dict[current_index])
        if current_index not in self._partial_empty:
            self._partial_empty.append(current_index)
        while stack_size == 0:
            current_index = self._used[-1]
            if current_index in self._partial_empty:
                self._partial_empty.pop()
            self._used.pop()
            stack_size = len(self._stacks_dict[self._used[-1]]) if len(self._used) else 1


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(2)
# obj.push(1)
# obj.push(2)
# obj.push(3)
# obj.push(4)
# obj.push(5)
# obj.popAtStack(0)
# obj.push(20)
# obj.push(21)
# obj.popAtStack(1)
# obj.popAtStack(1)
# obj.popAtStack(2)
# obj.popAtStack(2)
# obj.pop()
# obj.pop()
# obj.pop()
# obj.pop()
# obj.pop()
# obj.pop()
# obj.pop()
# obj.pop()