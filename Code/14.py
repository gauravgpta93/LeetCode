class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) <= 0:
            return ""
        return self._divide_and_conquer(strs, 0, len(strs) - 1)

    def _divide_and_conquer(self, string_list, left, right):
        if left == right:
            return string_list[left]
        else:
            mid = (left + right) // 2
            left_lcp = self._divide_and_conquer(string_list, left, mid)
            right_lcp = self._divide_and_conquer(string_list, mid + 1, right)
            return self._find_min_lcp(left_lcp, right_lcp)

    def _find_min_lcp(self, string_1, string_2):
        min_lenght = min(len(string_1), len(string_2))
        for index in range(min_lenght):
            if string_1[index] != string_2[index]:
                return string_1[:index]
        return string_1[:min_lenght]
