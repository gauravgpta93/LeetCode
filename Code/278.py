# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0, n + 1
        while left < right:
            mid = (left + right) // 2
            val = isBadVersion(mid)
            val_next = isBadVersion(mid + 1)
            if not val and val_next:
                return mid + 1
            if val:
                right = mid
            else:
                left = mid + 1
        return 0
