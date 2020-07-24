from threading import Condition


class Foo:
    def __init__(self):
        self._condition = Condition()
        self._first = True
        self._second = False
        self._third = False

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        with self._condition:
            printFirst()
            self._second = True
            self._condition.notify_all()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        with self._condition:
            self._condition.wait_for(lambda: self._second is True)
            printSecond()
            self._third = True

    def third(self, printThird: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.
        with self._condition:
            self._condition.wait_for(lambda: self._third is True)
            printThird()
