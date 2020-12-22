class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        temp_min, temp_max = A[0], A[-1]
        min_diff = temp_max - temp_min
        for i in range(0, len(A) - 1):
            t1_min, t2_max = A[i], A[i + 1]
            min_diff = min(min_diff, max(temp_max - K, t1_min + K) - min(temp_min + K, t2_max - K))
        return min_diff
