/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */

var maxPathSum = function(root) {
  var globalMaxPath = { value: -Infinity };

  findMaxPath(root, globalMaxPath);

  return globalMaxPath.value;
}


var findMaxPath = function(root, globalMaxPath) {
  if (!root) {
    return 0;
  }

  let left = 0, right = 0;
  if (root.left) {
    left = findMaxPath(root.left, globalMaxPath)
  }

  if (root.right) {
    right = findMaxPath(root.right, globalMaxPath)
  }
  let maxSubtreePath = Math.max(root.val + Math.max(left, right), root.val);
  let maxNodePath = Math.max(maxSubtreePath, root.val + left + right);

  if (maxNodePath > globalMaxPath.value) {
    globalMaxPath.value = maxNodePath;
  }

  return maxSubtreePath;
};
