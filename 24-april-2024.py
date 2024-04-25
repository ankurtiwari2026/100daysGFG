class Solution:
    def ways(self, n,m):
        mod = (10 ** 9) + 7
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j]=(dp[i-1][j]+dp[i][j-1])%mod
        return dp[n][m]