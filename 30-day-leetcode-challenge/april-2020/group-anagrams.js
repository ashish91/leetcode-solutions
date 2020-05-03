/**
 * @param {string[]} strs
 * @return {string[][]}
 */
let newArray = (size, defaultValue) => {
  let array = new Array(size);

  for (let i = 0; i < size; i++) {
    array[i] = defaultValue;
  }
  return array;
}

var groupAnagrams = function(strs) {
  let groupedAnagrams = {}, charCount, baseOrdinal = 'a'.charCodeAt(0);

  for (let i = 0; i < strs.length; i++) {
    charCount = newArray(26, 0);

    for (let j = 0; j < strs[i].length; j++) {
      let ordinal = strs[i].charCodeAt(j);
      charCount[ordinal - baseOrdinal] = charCount[ordinal - baseOrdinal] || 0;
      charCount[ordinal - baseOrdinal] += 1;
    }

    charCount = charCount.join('');
    groupedAnagrams[charCount] = groupedAnagrams[charCount] || [];
    groupedAnagrams[charCount].push(strs[i]);
  }

  let anagrams = [];
  for (key in groupedAnagrams) {
    anagrams.push(groupedAnagrams[key]);
  }
  return anagrams;
};
