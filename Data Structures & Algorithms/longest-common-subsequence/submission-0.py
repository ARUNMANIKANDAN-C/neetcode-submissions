class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for j in range(1, n + 1):
            for i in range(1, m + 1):
                k = 0

                if text1[i - 1] == text2[j - 1]:
                    k = 1

                dp[j][i] = max(
                    dp[j - 1][i],
                    dp[j][i - 1],
                    dp[j - 1][i - 1] + k
                )

        return dp[n][m]