class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        nums.sort()
        last_value = increase = 0
        for index, val in enumerate(nums):
            if index > 0 and val == nums[index - 1]:
                ans += [r + [val] for r in ans[last_value:]]
                last_value += increase
            else:
                last_value = increase = len(ans)
                ans += [r + [val] for r in ans]

        return ans
