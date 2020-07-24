from threading import Condition


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self._condition = Condition()
        self._counter = 1

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for i in range((self.n // 3) - (self.n // 15)):
            with self._condition:
                self._condition.wait_for(lambda: self._counter % 3 == 0 and self._counter % 15 != 0)
                printFizz()
                self._counter += 1
                self._condition.notify_all()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for i in range((self.n // 5) - (self.n // 15)):
            with self._condition:
                self._condition.wait_for(lambda: self._counter % 5 == 0 and self._counter % 15 != 0)
                printBuzz()
                self._counter += 1
                self._condition.notify_all()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(self.n // 15):
            with self._condition:
                self._condition.wait_for(lambda: self._counter % 15 == 0)
                printFizzBuzz()
                self._counter += 1
                self._condition.notify_all()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        n = self.n
        free_numbers = n - (n // 3) - (n // 5) + (n // 15)
        used = 0
        with self._condition:
            for i in range(free_numbers):
                self._condition.wait_for(lambda: self._counter % 3 != 0 and self._counter % 5 != 0)
                printNumber(self._counter)
                self._counter += 1
                self._condition.notify_all()
