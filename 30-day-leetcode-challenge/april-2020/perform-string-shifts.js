/**
 * @param {string} s
 * @param {number[][]} shift
 * @return {string}
 */
var stringShift = function(s, shift) {
  let trueShift = 0;

  for (let i = 0; i<shift.length; i++) {
    trueShift += shift[i][0] == 0 ? -shift[i][1] : shift[i][1];
  }

  trueShift = trueShift % s.length;

  if (trueShift == 0) {
    return s;
  }
  let shifted = new Array(s.length);
  for (let i = 0; i < s.length; i++) {
    if (i + trueShift >= 0) {
      shifted[(i + trueShift) % s.length] = s[i];
    } else {
      shifted[s.length + i + trueShift] = s[i]
    }
  }

  return shifted.join('');
};
