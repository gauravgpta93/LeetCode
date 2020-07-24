class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        if s1_len > s2_len:
            return False

        start, end = 0, 0
        l1 = [0] * 26
        l2 = [0] * 26
        for s in s1:
            l1[self._int_char(s)] += 1
        while end < s2_len:
            character_number = self._int_char(s2[end])
            if l1[character_number] == 0:
                l2 = [0] * 26
                start = end + 1
                end = start
            else:
                while l2[character_number] == l1[character_number]:
                    start_number = self._int_char(s2[start])
                    l2[start_number] -= 1
                    start += 1
                l2[character_number] += 1
                end += 1
                if end - start == len(s1):
                    return True
        return False

    def _int_char(self, s):
        return ord(s) - 97
