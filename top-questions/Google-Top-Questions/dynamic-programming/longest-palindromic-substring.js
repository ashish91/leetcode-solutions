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
