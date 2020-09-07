class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        current, left = 0, 0
        while left < len(nums):
            if nums[left] != 0:
                nums[left], nums[current] = nums[current], nums[left]
                current += 1
            left += 1
