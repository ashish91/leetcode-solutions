class Solution:
  def bottomUp(self, d, f, target):
    dp = [[0 for c in range(target+1)] for r in range(d+1) ]
    dp[0][0] = 1

    for i in range(1, d+1):
      for j in range(1, f+1):
        for k in range(j, target+1):
          dp[i][k] = (dp[i][k] + dp[i-1][k-j]) % 1000000007

    return dp[d][target]

  def numRollsToTarget(self, d: int, f: int, target: int) -> int:
    return self.bottomUp(d, f, target)