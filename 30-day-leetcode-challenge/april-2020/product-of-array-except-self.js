/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
  if (nums.length < 2) {
    return nums;
  }
  let product = new Array(nums.length);

  product[nums.length - 1] = nums[nums.length - 1];
  for (let i = nums.length - 2; i > 0; i--) {
    product[i] = product[i+1] * nums[i];
  }
  product[0] = product[1];

  let left = nums[0], i;
  for (i = 1; i < nums.length - 1; i++) {
    product[i] = left * product[i+1];
    left *= nums[i];
  }
  product[i] = left;

  return product;
};
