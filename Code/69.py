class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            if mid ** 2 <= x < (mid + 1) ** 2:
                return mid
            if mid ** 2 > x:
                right = mid - 1
            else:
                left = mid + 1
        return 0