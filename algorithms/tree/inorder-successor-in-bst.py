# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
    self.successor = None
    def dfs(root, p):
      if not root:
        return None

      dfs(root.left, p)
      if root.val > p.val:
        self.successor = root
        dfs(root.left, p)
      else:
        dfs(root.right, p)
    dfs(root, p)
    return self.successor
