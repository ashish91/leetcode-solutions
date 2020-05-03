/**
 * @param {string} J
 * @param {string} S
 * @return {number}
 */
var numJewelsInStones = function(J, S) {
  let jewels = {};

  for (let i = 0; i < J.length; i++) {
    jewels[J[i]] = 1;
  }

  let stones = 0;
  for (let i = 0; i < S.length; i++) {
    if (jewels[S[i]]) {
      stones += 1;
    }
  }

  return stones;
};
