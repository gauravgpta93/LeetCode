from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if not n:
            return [[]]

        left = top = 0
        right = bottom = n
        current = 1
        ans = [[0] * n for _ in range(n)]
        while current <= n * n:
            for i in range(left, right):
                ans[top][i] = current
                current += 1
            top += 1
            for i in range(top, bottom):
                ans[i][right - 1] = current
                current += 1
            right -= 1
            for i in range(right - 1, left - 1, -1):
                ans[bottom - 1][i] = current
                current += 1
            bottom -= 1
            for i in range(bottom - 1, top - 1, -1):
                ans[i][left] = current
                current += 1
            left += 1
        return ans


if __name__ == '__main__':
    Solution().generateMatrix(3)
