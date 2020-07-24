class Solution:
    def longestPalindrome(self, s: str) -> str:
        string_len = len(s)
        if string_len <= 1:
            return s
        start = end = 0
        max_len = 1
        for index in range(string_len):
            odd = self.get_from_center(s, index, index)
            even = self.get_from_center(s, index, index + 1)
            local_max = max(odd, even)
            if max_len < local_max:
                start = index - ((local_max - 1) // 2)
                end = index + (local_max // 2)
                max_len = local_max

        return s[start:end + 1]

    def get_from_center(self, string, left, right):
        while left >= 0 and right < len(string) and string[left] == string[right]:
            left -= 1
            right += 1
        return right - left - 1
