// DP Solution.
// Time Complexity: O(N^2)
// Space Complexity: O(N^2)

/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
  if (s.length < 2) {
    return s;
  }

  let dp = [];
  let longestPalindromeStart = 0, longestPalindromeEnd = 0;

  for (let i = 0; i < s.length; i++) {
    dp.push(new Array(s.length));

    dp[i][i] = true;
    dp[i][i+1] = s[i] == s[i+1];

    if(dp[i][i+1]) {
      longestPalindromeStart = i;
      longestPalindromeEnd = i+1;
    }
  }

  for (let i = s.length - 3; i >= 0; i--) {
    for (let j = i+2; j < s.length; j++) {
      dp[i][j] = dp[i+1][j-1] && s[i] == s[j];

      if (dp[i][j] && longestPalindromeEnd-longestPalindromeStart < j-i) {
        longestPalindromeStart = i;
        longestPalindromeEnd = j;
      }
    }
  }

  return s.substring(longestPalindromeStart, longestPalindromeEnd+1);
};
