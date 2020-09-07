class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        left, right = 0, len(A) - 1
        while left < right:
            if A[left] % 2 == 0:
                left += 1
            else:
                A[right], A[left] = A[left], A[right]
                right -= 1
        return A
