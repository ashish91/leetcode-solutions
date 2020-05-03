/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
  let length = nums.length;
  let maxAtPosition = new Array(length);
  let max = nums[0];

  maxAtPosition[0] = nums[0];
  for (let i = 1; i < length; i++) {
    maxAtPosition[i] = Math.max(maxAtPosition[i-1] + nums[i], nums[i] );
    max = Math.max(max, maxAtPosition[i]);
  }

  return max;
};
