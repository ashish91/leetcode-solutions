/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var removeDuplicates = function(s, k) {
  if (s.length < k) {
    return s;
  }

  let stack = [];
  let top;
  for (let i = 0; i < s.length; i++) {
    if (i == 0 || s[i] != s[i-1]) {
      stack.push(1);
    } else {
      top = stack.pop();
      top += 1;
      if (top == k) {
        s = s.slice(0, i-k+1) + s.slice(i+1);
        i = i - k;
      } else {
        stack.push(top);
      }
    }
  }

  return s;
};
