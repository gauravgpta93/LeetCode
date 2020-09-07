class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even, odd = 0, 1
        even_increment = True

        while even < len(A) and odd < len(A):
            if even_increment:
                if A[even] % 2 == 0:
                    even += 2
                    even_increment = not even_increment
                else:
                    A[even], A[odd] = A[odd], A[even]
                    odd += 2
            else:
                if A[odd] % 2 == 1:
                    odd += 2
                    even_increment = not even_increment
                else:
                    A[even], A[odd] = A[odd], A[even]
                    even += 2
        return A