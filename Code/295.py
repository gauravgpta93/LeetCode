import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queues = [], []

    def addNum(self, num: int) -> None:
        lo, hi = self.queues
        heapq.heappush(lo, -heapq.heappushpop(hi, num))
        if len(lo) > len(hi):
            heapq.heappush(hi, -heapq.heappop(lo))

    def findMedian(self) -> float:
        lo, hi = self.queues
        if len(lo) == len(hi):
            return (-lo[0] + hi[0]) / 2
        return float(hi[0])

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
