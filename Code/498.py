from typing import List


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        up = True
        if not matrix:
            return list()
        row, col = len(matrix) - 1, len(matrix[0]) - 1
        i, j = 0, 0
        ans = list()
        while i != row or j != col:
            ans.append(matrix[i][j])
            if up:
                if i == 0 or j == col:
                    up = False
                    if i == 0 and j == col:
                        i = 1
                        j = col
                    elif i == 0:
                        j += 1
                    elif j == col:
                        i += 1
                else:
                    i -= 1
                    j += 1
            else:
                if i == row or j == 0:
                    up = True
                    if i == row and j == 0:
                        j = 1
                    elif i == row:
                        j += 1
                    elif j == 0:
                        i += 1
                else:
                    i += 1
                    j -= 1
        ans.append(matrix[row][col])
        return ans


if __name__ == '__main__':
    l1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(Solution().findDiagonalOrder(l1))
