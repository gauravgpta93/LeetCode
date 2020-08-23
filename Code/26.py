class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, current = 0, 0
        while current < len(nums) - 1:
            if nums[left] == nums[current + 1]:
                current += 1
            else:
                nums[left+1] = nums[current+1]
                current += 1
                left += 1
        return left + 1 if len(nums) else 0
