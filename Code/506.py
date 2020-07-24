class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        sorted_list = sorted(nums)[::-1]
        top_dict = dict()
        for i, val in enumerate(sorted_list):
            if i < 3:
                top_dict[val] = ["Gold", "Silver", "Bronze"][i] + " Medal"
            else:
                top_dict[val] = str(i)
        return [top_dict.get(num) for num in nums]

