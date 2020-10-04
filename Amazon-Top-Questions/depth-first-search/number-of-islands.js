
/**
 * @param {character[][]} grid
 * @return {number}
 */
var markOnes = function(grid, row, col, rowsize, colsize) {
  if (row < 0 || row >= rowsize || col < 0 || col >= colsize || grid[row][col] == '0') {
    return;
  }

  grid[row][col] = '0';
  markOnes(grid, row + 1, col, rowsize, colsize);
  markOnes(grid, row - 1, col, rowsize, colsize);
  markOnes(grid, row, col + 1, rowsize, colsize);
  markOnes(grid, row, col - 1, rowsize, colsize);
}

var numIslands = function(grid) {
    if (grid.length == 0) {
        return 0;
    }

  var colsize = grid[0].length, rowsize = grid.length, islands = 0;
  for (let i = 0; i < rowsize; i++) {
    for (let j = 0; j < colsize; j++) {
      if (grid[i][j] == '1') {
        islands++;
        markOnes(grid, i, j, rowsize, colsize);
      }
    }
  }

  return islands;
};