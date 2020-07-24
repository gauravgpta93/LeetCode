class DoubleLinkedStruct:
    def __init__(self, val, forward=None, backward=None):
        self.forward = forward
        self.backward = backward
        self.val = val


class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.front = None
        self.back = None
        self.size = k
        self.current_size = 0

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.current_size >= self.size:
            return False

        if self.current_size == 0:
            self.front = self.back = DoubleLinkedStruct(value)
        else:
            temp = DoubleLinkedStruct(value, forward=self.front)
            self.front.backward, self.front = temp, temp

        self.current_size += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.current_size >= self.size:
            return False

        if self.current_size == 0:
            return self.insertFront(value)
        else:
            temp = DoubleLinkedStruct(value, backward=self.back)
            self.back.forward, self.back = temp, temp
        self.current_size += 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.current_size == 0:
            return False
        else:
            if self.current_size == 1:
                self.front = self.back = None
            else:
                self.front.forward, self.front = None, self.front.forward
                self.front.backward = None
        self.current_size -= 1
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.current_size == 0:
            return False
        else:
            if self.current_size == 1:
                self.front = self.back = None
            else:
                self.back.backward, self.back = None, self.back.backward
                self.back.forward = None
        self.current_size -= 1
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return self.front.val if self.front else -1

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return self.back.val if self.back else -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.current_size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.current_size == self.size


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(3)
# param_1 = obj.insertFront(2)
# param_2 = obj.insertLast(3)
# param_2 = obj.insertLast(3)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
