class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        increasing = True
        if len(A) < 3:
            return False
        if A[0] > A[1]:
            return False
        for index in range(1, len(A)):
            num = A[index]
            prev = A[index - 1]
            if num == prev:
                return False
            if increasing:
                if num < prev:
                    increasing = False
            else:
                if num > prev:
                    return False
        return True if not increasing else False
