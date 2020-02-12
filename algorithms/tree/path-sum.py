# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def hasPathSum(self, root: TreeNode, sum: int, parentSum: int = 0) -> bool:
    if root is None:
      return False
    elif root.left is None and root.right is None:
      return parentSum + root.val == sum

    return self.hasPathSum(root.left, sum, parentSum + root.val) or self.hasPathSum(root.right, sum, parentSum + root.val)
