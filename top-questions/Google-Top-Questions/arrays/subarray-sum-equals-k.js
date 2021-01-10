/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraySum = function(nums, k) {
  let sum = 0, count = 0;

  for (let start = 0; start < nums.length; start++) {
    sum = 0;
    for (let end = start; end < nums.length; end++) {
      sum += nums[end];
      if (sum == k) {
        count += 1;
      }
    }
  }

  return count;
};