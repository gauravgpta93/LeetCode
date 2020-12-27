class Solution:
    def numDecodings(self, s: str) -> int:
        if s == "" or s[0] == "0":
            return 0
        dp = [0] * (len(s) + 1)
        dp[:2] = [1, 1]
        for index in range(2, len(s) + 1):
            if 0 < int(s[index - 1]):
                dp[index] += dp[index - 1]
            if 10 <= int(s[index - 2:index]) <= 26:
                dp[index] += dp[index - 2]
        return dp[-1]


if __name__ == '__main__':
    print(Solution().numDecodings("10"))
