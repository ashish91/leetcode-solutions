# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
  def sumEvenGrandparent(self, root: TreeNode) -> int:
    sum = 0
    def dfs(node, parent, grand):
      nonlocal sum

      if node is None:
        return

      if grand and grand.val%2 == 0:
        sum += node.val

      dfs(node.left, node, parent)
      dfs(node.right, node, parent)

    dfs(root, None, None)
    return sum
