from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        current, left = 0, 0
        while current < len(arr):
            if arr[left] == 0:
                current += 1
            current += 1
            left += 1

        if current == len(arr) + 1:
            current -= 2
            left -= 1
            arr[current] = 0

        while left > 0:
            current -= 1
            left -= 1
            arr[current] = arr[left]
            if arr[left] == 0:
                current -= 1
                arr[current] = 0
        return


if __name__ == '__main__':
    print(Solution().duplicateZeros([1, 0, 2, 1]))
