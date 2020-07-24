import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pointer_1 = pointer_2 = 0
        queue = []

        def add_to_queue(i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(queue, [nums1[i] + nums2[j], i, j])

        add_to_queue(0, 0)
        ans = []

        while queue and len(ans) < k:
            _, pointer_1, pointer_2 = heapq.heappop(queue)
            ans.append([nums1[pointer_1], nums2[pointer_2]])

            if pointer_2 == 0:
                add_to_queue(pointer_1 + 1, pointer_2)
            add_to_queue(pointer_1, pointer_2 + 1)
        return ans


if __name__ == '__main__':
    print(Solution().kSmallestPairs([1, 7, 11], [2, 4,12, 16], 16))
