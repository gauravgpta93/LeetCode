class Solution:
    def maxRotateFunction(self, A) -> int:
        function_sum = current_sum = sum(i * j for i, j in enumerate(A))
        total = sum(A)
        size = len(A)
        for i in range(len(A) - 1, 0, -1):
            current_sum += total - (size * A[i])
            function_sum = max(function_sum, current_sum)
        return function_sum


Solution().maxRotateFunction([4, 3, 2, 6])
