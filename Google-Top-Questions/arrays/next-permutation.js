/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */

let swap = function(nums, i, j) {
  let temp = nums[i];
  nums[i] = nums[j];
  nums[j] = temp;
}

let reverse = function(nums, start, end) {
  while (start <= end) {
    swap(nums, start, end);
    start += 1;
    end -= 1;
  }

  return nums;
}

var nextPermutation = function(nums) {
  let i = nums.length - 2;

  while (i >= 0 && nums[i+1] <= nums[i]) {
    i -= 1;
  }

  if (i >= 0) {
    let j = nums.length - 1;
    while (j >= 0 && nums[j] <= nums[i]) {
      j -= 1;
    }
    swap(nums, i, j);
  }

  reverse(nums, i+1, nums.length - 1);

  return nums;
};
