// Palindrom center based Solution.
// Time Complexity: O(N^2)
// Space Complexity: O(1)

/**
 * @param {string} s
 * @return {string}
 */

let oddPalindrome = (s, i) => {
  let length = 1, l = i-1, r = i+1;
  while (l >= 0 && r < s.length && s[l] == s[r]) {
    l -= 1;
    r += 1;
    length += 2;
  }

  return length;
}

let evenPalindrome = (s, i) => {
  let length = 0, l = i, r = i+1;
  while (l >= 0 && r < s.length && s[l] == s[r]) {
    l -= 1;
    r += 1;
    length += 2;
  }

  return length;
}

var longestPalindrome = function(s) {
  if (s.length < 2) {
    return s;
  }

  let len1, len2, len, start = 0, end = 0;
  for (let i = 0; i < s.length; i++) {
    len1 = oddPalindrome(s, i);
    len2 = evenPalindrome(s, i);
    len = Math.max(len1, len2);

    if (len > end - start) {
      start = i - Math.floor((len - 1)/2);
      end = i + Math.floor(len/2);
    }
  }

  return s.substring(start, end+1);
};

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
