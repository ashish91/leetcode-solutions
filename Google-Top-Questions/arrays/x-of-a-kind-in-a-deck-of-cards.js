/**
 * @param {number[]} deck
 * @return {boolean}
 */
let gcd = function(x, y) {
  return x == 0 ? y : gcd(y%x, x);
}

var hasGroupsSizeX = function(deck) {
  let count = new Map();
  for (let i in deck) {
    if (count.has(deck[i])) {
      count.set(deck[i], count.get(deck[i]) + 1);
    } else {
      count.set(deck[i], 1);
    }
  }

  let groups = -1;
  for (let [num, freq] of count) {
    if (freq > 0) {
      if (groups == -1) {
        groups = freq;
      } else {
        groups = gcd(groups, freq);
      }
    }
  }

  return groups >= 2;
};
