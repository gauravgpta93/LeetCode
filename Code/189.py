class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        count = 0
        while count < k:
            start = count
            current = start + k
            while start != current:
                next = (current + k) % len(nums)
                nums[start], nums[current] = nums[current], nums[next]
