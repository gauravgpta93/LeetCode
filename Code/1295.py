class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            if len(str(num)) & 1 == 0:
                result += 1
        return result
