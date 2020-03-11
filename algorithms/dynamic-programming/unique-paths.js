/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function(m, n) {
  let paths = Array.from(Array(m), () => new Array(n));

  for (let r = 0; r < m; r++) {
    paths[r][0] = 1;
  }

  for (let c = 0; c < n; c++) {
    paths[0][c] = 1;
  }

  for (let r = 1; r < m; r++) {
    for (let c = 1; c < n; c++) {
      paths[r][c] = paths[r-1][c] + paths[r][c-1];
    }
  }

  return paths[m-1][n-1];
};
