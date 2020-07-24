class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash = dict()
        for index, value in enumerate(nums):
            expected = target - value
            if expected in hash:
                expected_index = hash.get(expected, None)
                return (expected_index, index)
            hash[value] = index
        return (-1, -1)
