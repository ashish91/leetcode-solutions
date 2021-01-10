class Solution:
  def uniquePaths(self, m: int, n: int) -> int:
    if m == 0 or n == 0:
      return 0

    if m == 1 or n == 1:
      return 1

    dp = [[1 for j in range(m)] for i in range(n)]

    for i in range(1, n):
      for j in range(1, m):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[n-1][m-1]
