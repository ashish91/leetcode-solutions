// Normal DP
// Time Complexity: O(MN)
// Space Complexity: O(MN)

/**
 * @param {character[][]} matrix
 * @return {number}
 */
var maximalSquare = function(matrix) {
  if (matrix.length == 0) {
    return 0;
  }

  let rows = matrix.length, cols = matrix[0].length;
  let dp = [];
  for (let i = 0; i <= rows; i++) {
    dp.push(Array(cols+1).fill(0));
  }

  let maxSquare = 0;

  for (let i = 1; i <= rows; i++) {
    for (let j = 1; j <= cols; j++) {
      if (matrix[i-1][j-1] === '1') {
        dp[i][j] = Math.min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1;
        maxSquare = Math.max(maxSquare, dp[i][j]);
      }
    }
  }

  return maxSquare * maxSquare;
};

// Space Optimized DP
// Time Complexity: O(MN)
// Space Complexity: O(M+N)

/**
 * @param {character[][]} matrix
 * @return {number}
 */
var maximalSquare = function(matrix) {
  if (matrix.length == 0) {
    return 0;
  }

  let rows = matrix.length, cols = matrix[0].length;
  let dp = Array(cols+1).fill(0);
  let maxSquare = 0, temp, prev = 0;

  for (let i = 1; i <= rows; i++) {
    for (let j = 1; j <= cols; j++) {
      temp = dp[j];
      if (matrix[i-1][j-1] === '1') {
        dp[j] = Math.min(dp[j-1], prev, dp[j]) + 1;
        maxSquare = Math.max(maxSquare, dp[j]);
      } else {
        dp[j] = 0;
      }
      prev = temp;
    }
  }

  return maxSquare * maxSquare;
};
