class Solution:
  def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
    R = len(grid)
    C = len(grid[0])

    if grid[0][0] == 1:
      return 0

    grid[0][0] = 1
    for i in range(1, R):
      if grid[i][0] == 1:
        grid[i][0] = 0
      else:
        grid[i][0] = grid[i-1][0]

    for j in range(1, C):
      if grid[0][j] == 1:
        grid[0][j] = 0
      else:
        grid[0][j] = grid[0][j-1]

    for i in range(1, R):
      for j in range(1, C):
        if grid[i][j] == 1:
          grid[i][j] = 0
        else:
          grid[i][j] = grid[i-1][j] + grid[i][j-1]

    return grid[R-1][C-1]
