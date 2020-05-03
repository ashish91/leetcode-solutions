/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number[]} arr
 * @return {boolean}
 */
var isValidSequence = function(root, arr, index = 0) {
  if (!root) {
    return false;
  }

  if (arr[index] !== root.val) {
    return false;
  } else if (!root.left && !root.right && index === arr.length - 1) {
    return true;
  }

  return isValidSequence(root.left, arr, index + 1) || isValidSequence(root.right, arr, index + 1);
};
