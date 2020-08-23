class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        l, r = 0, len(A) - 1
        A = list(map(lambda x: x * x, A))
        result = [0] * (len(A))
        current = len(A) - 1
        while l <= r:
            left, right = A[l], A[r]
            if left > right:
                l += 1
                result[current] = left
            else:
                r -= 1
                result[current] = right
            current -= 1
        return result
