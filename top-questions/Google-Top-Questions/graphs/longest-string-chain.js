/**
 * @param {string[]} words
 * @return {number}
 */
let dfs = function(word, chain) {
  if (!chain[word]) {
    return 0;
  }

  if (chain[word] > 1) {
    return chain[word];
  }

  for (let i = 0; i < word.length; i++) {
    let newWord = word.substring(0, i).concat(word.substring(i+1, word.length));
    chain[word] = Math.max(chain[word], dfs(newWord, chain) + 1);
  }

  return chain[word];
}

var longestStrChain = function(words) {
  let chain = {};

  for (let i = 0; i < words.length; i++) {
    chain[words[i]] = 1;
  }

  for (let i = 0; i < words.length; i++) {
    dfs(words[i], chain);
  }

  let longestChain = 0;
  for (let i = 0; i < words.length; i++) {
    longestChain = Math.max(longestChain, chain[words[i]]);
  }

  return longestChain;
};
