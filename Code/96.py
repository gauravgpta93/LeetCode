class Solution:
    def numTrees(self, n: int) -> int:
        ans = [0] * (n + 1)
        ans[0] = 1
        for i in range(1, n + 1):
            for j in range(i):
                ans[i] += (ans[j] * ans[i - j - 1])
        return ans[n]
