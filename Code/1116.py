from threading import Condition


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self._condition = Condition()
        self._zero = True
        self._toggle = False

        # printNumber(x) outputs "x", where x is an integer.

    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            with self._condition:
                self._condition.wait_for(lambda: self._zero is True)
                printNumber(0)
                self._zero = False
                self._condition.notify_all()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        if self.n > 1:
            for i in range(2, self.n + 1, 2):
                with self._condition:
                    self._condition.wait_for(lambda: self._zero is False and self._toggle is True)
                    printNumber(i)
                    self._toggle = not self._toggle
                    self._zero = True
                    self._condition.notify_all()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        if self.n > 0:
            for i in range(1, self.n + 1, 2):
                with self._condition:
                    self._condition.wait_for(lambda: self._zero is False and self._toggle is False)
                    printNumber(i)
                    self._toggle = not self._toggle
                    self._zero = True
                    self._condition.notify_all()
