class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def _permute(current_path, remaining):
            if len(current_path) == len(nums):
                ans.append(current_path[:])
            else:
                for i, value in enumerate(remaining):
                    current_path.append(value)
                    _permute(current_path, remaining[:i] + remaining[i + 1:])
                    current_path.pop()

        ans = list()
        _permute(list(), nums)
        return ans
