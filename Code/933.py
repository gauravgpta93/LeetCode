from collections import deque


class RecentCounter:

    def __init__(self):
        self._queue = deque()

    def ping(self, t: int) -> int:
        while self._queue and self._queue[0] < t - 3000:
            self._queue.popleft()
        self._queue.append(t)
        return len(self._queue)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
