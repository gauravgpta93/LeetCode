class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        number_hash = set()
        return any(x in number_hash or number_hash.add(x) for x in nums)