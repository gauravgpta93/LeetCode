class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        count_dict = Counter(s)
        for index, value in enumerate(s):
            if count_dict[value] == 1:
                return index
        return -1
