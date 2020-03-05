/**
 * @param {string} S
 * @return {string}
 */
var removeDuplicates = function(S) {
  stack = []

  for (let i = 0; i < S.length; i++) {
    if (stack.length > 0 && stack[stack.length - 1] == S[i]) {
      stack.pop();
    } else {
      stack.push(S[i]);
    }

  }

  return stack.join('');
};
