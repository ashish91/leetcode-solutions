/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxLength = function(nums) {
  let cache = { 0: -1};
  let count = 0, max = 0;

  for (let i = 0; i < nums.length; i++) {
    count = count + (nums[i] == 1 ? 1 : -1);
    if (cache[count] != undefined) {
      max = Math.max(max, i - cache[count])
    } else {
      cache[count] = i;
    }
  }

  return max;
};
