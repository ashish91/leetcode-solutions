/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
  if (s.length == 0) {
    return true;
  }

  let stack = [s[0]], map = { '(':')', '{':'}', '[':']'}, top;
  for (let i = 1; i < s.length; i++) {
    top = stack[stack.length - 1];
    if (s[i] == map[top]) {
      stack.pop(s[i]);
    } else {
      stack.push(s[i]);
    }
  }

  return stack.length == 0;
};
