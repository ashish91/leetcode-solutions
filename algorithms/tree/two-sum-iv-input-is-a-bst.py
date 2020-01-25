# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

  def traversal(self, root, aux, target: int) -> bool:
    if root is None:
      return False

    if (target - root.val) in aux:
      return True
    aux[root.val] = True

    return self.traversal(root.left, aux, target) or self.traversal(root.right, aux, target)

  def findTarget(self, root: TreeNode, k: int) -> bool:
    return self.traversal(root, {}, k)
