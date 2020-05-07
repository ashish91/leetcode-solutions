# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def __init__(self):
    # To save the depth of the first node.
    self.currentDepth = None
    self.isCousin = False

  def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
    self.dfs(root, 0, x, y)
    return self.isCousin

  def dfs(self, node: TreeNode, depth: int, x: int, y: int) -> bool:
    if node is None:
      return False

    if self.currentDepth and depth > self.currentDepth:
      return False

    if node.val == x or node.val == y:
      if self.currentDepth is None:
        self.currentDepth = depth
      return self.currentDepth == depth

    left = self.dfs(node.left, depth+1, x, y)
    right = self.dfs(node.right, depth+1, x, y)

    if left and right and self.currentDepth != depth + 1:
      self.isCousin = True

    return left or right
