class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        start, end, longest_sub_string = 0, 1, 1
        hash = set()
        hash.add(s[0])
        while end < len(s):
            while s[end] in hash:
                hash.remove(s[start])
                start += 1
            hash.add(s[end])
            longest_sub_string = max(longest_sub_string, end-start+1)
            end += 1
        return longest_sub_string
