/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function(s) {
  let seen = Math.pow(2, 26), code, binary, repeating = Math.pow(2, 26);
  for (let i = 0; i < s.length; i++) {
    code = s.charCodeAt(i) - 97;
    binary = Math.pow(2, code);
    if (binary & seen) {
      repeating = repeating | binary;
    } else {
      seen = seen | binary;
    }
  }

  for (let i = 0; i < s.length; i++) {
    code = s.charCodeAt(i) - 97;
    binary = Math.pow(2, code);
    if ((binary & repeating) == 0) {
      return i;
    }
  }

  return -1;
};
