class Solution:
    def compress(self, chars: List[str]) -> int:
        write = left = right = 0
        while right < len(chars):
            if right + 1 == len(chars) or chars[left] != chars[right + 1]:
                chars[write] = chars[left]
                write += 1
                if right > left:
                    for digit in str(right - left + 1):
                        chars[write] = digit
                        write += 1
                left = right + 1
            right += 1
        return write
