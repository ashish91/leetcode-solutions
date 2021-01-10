/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
  if (height.length == 0) {
    return 0;
  }

  let leftMax = Array(height.length).fill(0), rightMax = Array(height.length).fill(0);

  let max = height[0];
  for (let i = 0; i < height.length; i++) {
    if (max < height[i]) {
      max = height[i];
    }
    leftMax[i] = max;
  }

  max = height[height.length - 1];
  for (let i = height.length - 1; i >= 0; i--) {
    if (max < height[i]) {
      max = height[i];
    }
    rightMax[i] = max;
  }

  let trappedWater = 0;
  for (let i = 0; i < height.length; i++) {
    trappedWater += Math.min(leftMax[i], rightMax[i]) - height[i];
  }

  return trappedWater;
};
