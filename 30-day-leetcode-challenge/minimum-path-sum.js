/**
 * @param {number[][]} grid
 * @return {number}
 */
var minPathSum = function(grid) {
  for (let i = 1; i < grid.length; i++) {
    grid[i][0] += grid[i-1][0];
  }
  for (let i = 1; i < grid[0].length; i++) {
    grid[0][i] += grid[0][i-1];
  }

  for (let r = 1; r < grid.length; r++) {
    for (let c = 1; c < grid[0].length; c++) {
      grid[r][c] += Math.min(grid[r-1][c], grid[r][c-1]);
    }
  }

  return grid[grid.length-1][grid[0].length-1];
};
