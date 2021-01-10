/**
 * @param {string[]} words
 * @return {number}
 */
let dpSearch = function(words, chain) {
  for (let w = 0; w < words.length; w++) {
    for (let c = 0; c < words[w].length; c++) {
      let newWord = words[w].substring(0, c).concat(words[w].substring(c+1, words[w].length));
      chain[words[w]] = Math.max(chain[words[w]], (chain[newWord] || 0) + 1);
    }
  }

  return chain;
}

var longestStrChain = function(words) {
  words = words.sort((w1, w2) => w1.length - w2.length);

  let chain = {};
  for (let i = 0; i < words.length; i++) {
    chain[words[i]] = 1;
  }

  chain = dpSearch(words, chain);

  let longestChain = 0;
  for (let i = 0; i < words.length; i++) {
    longestChain = Math.max(longestChain, chain[words[i]]);
  }

  return longestChain;
};
