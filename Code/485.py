class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_length = max_length = 0
        for index, value in enumerate(nums):
            if value == 1:
                current_length += 1
            else:
                max_length = max(max_length, current_length)
                current_length = 0
        return max(max_length, current_length)
