/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
  let zeroes = 0, zeroIndex = -1;

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] == 0) {
      zeroes += 1;
      if (zeroIndex == -1) {
        zeroIndex = i;
      }
    } else if (zeroIndex >= 0){
      nums[zeroIndex] = nums[i];
      zeroIndex += 1;
    }
  }

  while (zeroIndex >= 0 && zeroIndex < nums.length) {
    nums[zeroIndex] = 0;
    zeroIndex += 1;
  }
  return nums;
};
