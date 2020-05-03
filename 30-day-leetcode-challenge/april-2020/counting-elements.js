/**
 * @param {number[]} arr
 * @return {number}
 */
var countElements = function(arr) {
  if (arr.length < 2) {
    return 0;
  }

  let countHash = {};
  for (let i = 0; i < arr.length; i++) {
    if (countHash[arr[i]] === undefined) {
      countHash[arr[i]] = 0;
    }
    countHash[arr[i]] += 1;
  }

  let count = 0;
  for (let key in countHash) {
    if (countHash[parseInt(key)+1] != undefined) {
      count += countHash[key];
    }
  }

  return count;
};
