class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        max_len = len(nums)
        for num in nums:
            if num > max_len:
                continue
            nums[abs(num) - 1] = -abs(nums[abs(num) - 1])
        res = list()
        for index, num in enumerate(nums):
            if num > 0:
                res.append(index + 1)
        return res
