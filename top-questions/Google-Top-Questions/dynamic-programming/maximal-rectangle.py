# DP on Histograms
# T: O(MN*M)
# S: O(MN)
class Solution:
  def maximalRectangle(self, matrix: List[List[str]]) -> int:
    R = len(matrix)
    if R == 0:
      return 0

    C = len(matrix[0])

    dp = [[0 for c in range(C)] for r in range(R)]

    maxarea = 0
    for i in range(R):
      for j in range(C):
        if matrix[i][j] == '1':
          if j == 0:
            dp[i][j] = 1
          else:
            dp[i][j] = dp[i][j-1]+1

          width = dp[i][j]
          for k in range(i,-1,-1):
            width = min(width, dp[k][j])
            maxarea = max(maxarea, width*(i-k+1))

    return maxarea