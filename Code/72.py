class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len_w1 = len(word1)
        len_w2 = len(word2)
        dp = [[0] * (len_w2 + 1) for _ in range(len_w1 + 1)]
        for i in range(len_w1 + 1):
            dp[i][0] = i
        for i in range(len_w2 + 1):
            dp[0][i] = i

        for i in range(1, len_w1 + 1):
            for j in range(1, len_w2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    replace = dp[i - 1][j - 1]
                    insert = dp[i][j - 1]
                    delete = dp[i - 1][j]
                    dp[i][j] = 1 + min(replace, insert, delete)
        return dp[-1][-1]
