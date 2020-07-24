class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        from collections import Counter
        count = Counter(nums)
        ans = list()
        self._permute(list(), len(nums), count, ans)
        return ans

    def _permute(self, current_path, total_size, count_dict, ans):
        if len(current_path) == total_size:
            ans.append(current_path[:])
        else:
            for key in count_dict:
                if count_dict[key] > 0:
                    current_path.append(key)
                    count_dict[key] -= 1
                    self._permute(current_path, total_size, count_dict, ans)
                    count_dict[key] += 1
                    current_path.pop()
