# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            mid = (left + right) // 2
            val = guess(mid)
            if val == 0:
                return mid
            if val == -1:
                right = mid - 1
            else:
                left = mid + 1
        return 0
