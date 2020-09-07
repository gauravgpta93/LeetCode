from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        for index in range(len(arr)):
            num = arr[index]
            if (num / 2) in arr[:index] + arr[index + 1:]:
                return True
        return False


if __name__ == '__main__':
    print(Solution().checkIfExist([0,2]))
