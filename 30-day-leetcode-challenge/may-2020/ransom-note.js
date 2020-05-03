/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function(ransomNote, magazine) {
  if (ransomNote.length > magazine.length) {
    return false;
  }

  let letters = {};

  for (let i = 0; i < magazine.length; i++) {
    if (letters[magazine[i]] === undefined) {
      letters[magazine[i]] = 0;
    }
    letters[magazine[i]] += 1;
  }

  for (let i = 0; i < ransomNote.length; i++) {
    if ((letters[ransomNote[i]] === undefined) || letters[ransomNote[i]] == 0) {
      return false;
    }
    letters[ransomNote[i]] -= 1;
  }

  return true;
};
