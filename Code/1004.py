class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        current_length = max_length = 0
        import queue
        q = queue.Queue(maxsize=K)
        if K > 0:
            q.put(-1)
        for index, value in enumerate(A):
            if value == 1:
                current_length += 1
            else:
                if not q.full() and K > 0:
                    q.put(index)
                    current_length += 1
                else:
                    max_length = max(max_length, current_length)
                    last = q.get() if K > 0 else index
                    current_length = index - last
                    q.put(index)
        return max(max_length, current_length)
