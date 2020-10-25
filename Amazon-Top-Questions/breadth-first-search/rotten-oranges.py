class Solution:
  def orangesRotting(self, grid: List[List[int]]) -> int:
    queue = []
    fresh = 0

    R = len(grid)
    C = len(grid[0])

    for i in range(R):
      for j in range(C):
        if grid[i][j] == 2:
          queue.append([i,j])
        elif grid[i][j] == 1:
          fresh += 1

    directions = [(-1,0), (0,-1), (1,0), (0,1)]
    levels = 0
    while len(queue) > 0:
      levels += 1
      neighbours = []
      for row, col in queue:
        for d in directions:
          nrow, ncol = row + d[0], col + d[1]
          if R > nrow >= 0 and C > ncol >= 0:
            if grid[nrow][ncol] == 1:
              neighbours.append((nrow,ncol))
              fresh -= 1
              grid[nrow][ncol] = 0

      queue = neighbours

    return max(levels-1,0) if fresh == 0 else -1