class Solution:
    @staticmethod
    def lcs(X, Y, m, n, dp):
        if m == 0 or n == 0:
            return 0

        if dp[m][n] != -1:
            return dp[m][n]

        if X[m - 1] == Y[n - 1]:
            dp[m][n] = 1 + Solution.lcs(X, Y, m - 1, n - 1, dp)
            return dp[m][n]

        dp[m][n] = max(Solution.lcs(X, Y, m, n - 1, dp), Solution.lcs(X, Y, m - 1, n, dp))
        return dp[m][n]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
        return self.lcs(text1, text2, m, n, dp)