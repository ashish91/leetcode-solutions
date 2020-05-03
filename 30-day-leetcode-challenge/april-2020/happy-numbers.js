/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
  let sadNumbers = {};

  let next = n;
  while (!sadNumbers[next] && next != 1) {
    sadNumbers[next] = true;

    n = next;
    next = 0;
    while(n > 0) {
      next += (n%10)**2;
      n = parseInt(n/10);
    }
  }

  if (next == 1) {
    return true;
  } else if (sadNumbers[next]) {
    return false;
  }
};
