import threading


class FooBar:
    def __init__(self, n):
        self.n = n
        self._foo_lock = threading.Lock()
        self._boo_lock = threading.Lock()
        self._boo_lock.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.\
            self._foo_lock.acquire()
            printFoo()
            self._boo_lock.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            # printBar() outputs "bar". Do not change or remove this line.
            self._boo_lock.acquire()
            printBar()
            self._foo_lock.release()
