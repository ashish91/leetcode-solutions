/**
 * @param {string} S
 * @param {string} T
 * @return {boolean}
 */
let process = (s) => {
  let stack = [];

  for (let c of s) {
    if (c == '#') {
      stack.pop();
    } else {
      stack.push(c);
    }
  }

  return stack.join('');
}

var backspaceCompare = function(S, T) {
  return process(S) == process(T);
};
