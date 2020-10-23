import itertools
from typing import List


class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:

        max_time = -1
        # max_time = self.permutate(arr, max_time, 0)
        max_time = self.inbuild_function(arr)
        if max_time == -1:
            return ""
        else:
            return "{:02d}:{:02d}".format(max_time // 60, max_time % 60)

    def get_time(self, arr, max_time):
        h1, h2, m1, m2 = arr
        hour = h1 * 10 + h2
        minutes = m1 * 10 + m2
        if hour < 24 and minutes < 60:
            max_time = max(max_time, hour * 60 + minutes)
        return max_time

    def permutate(self, arr, max_time, start):

        max_time = self.get_time(arr, max_time)

        if start == len(arr):
            return max_time

        for index in range(start, len(arr)):
            if index == start:
                continue
            arr[start], arr[index] = arr[index], arr[start]
            max_time = self.permutate(arr, max_time, start + 1)
            arr[start], arr[index] = arr[index], arr[start]

        return max_time

    def inbuild_function(self, arr: List[int]) -> str:
        max_time = -1
        for temp in itertools.permutations(arr):
            max_time = self.get_time(temp, max_time)
        return max_time


if __name__ == '__main__':
    print(Solution().largestTimeFromDigits([1, 2, 3, 4]))
