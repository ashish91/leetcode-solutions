/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isValidBST = function(root, lower = -Infinity, upper = Infinity) {
  if (!root) {
    return true;
  }

  let validNode = (lower < root.val) && (upper > root.val);
  return validNode && isValidBST(root.left, lower, root.val) && isValidBST(root.right, root.val, upper);
};
