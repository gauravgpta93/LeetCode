import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        generator_series = map(lambda row: ([row + col, row, col] for col in nums2), nums1)
        heapq_series = heapq.merge(*generator_series)
        ans = list()
        for i, minimum in enumerate(heapq_series):
            if i == k:
                break
            ans.append(minimum[1:])
        return ans
