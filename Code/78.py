class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for val in nums:
            ans += [r + [val] for r in ans]
        return ans
