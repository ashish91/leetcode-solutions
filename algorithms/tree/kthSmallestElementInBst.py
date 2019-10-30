# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
      stack = [root]
      current = root
      while current or stack:
        while current:
          stack.append(current)
          current = current.left

        current = stack.pop()
        k = k - 1
        if k == 0:
          return current.val
        current = current.right
