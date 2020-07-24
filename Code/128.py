class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        longest = current = 1

        for num in nums:
            if num - 1 not in num_set:
                next_val = num + 1
                while next_val in num_set:
                    current += 1
                    next_val += 1
                longest = max(longest, current)
                current = 1
        return longest
