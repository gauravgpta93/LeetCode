class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        value_index_dict = defaultdict(list)
        for x, value in enumerate(nums):
            if len(value_index_dict[value]) > 0:
                if abs(x - value_index_dict[value][-1]) <= k:
                    return True
            value_index_dict[value].append(x)
        return False