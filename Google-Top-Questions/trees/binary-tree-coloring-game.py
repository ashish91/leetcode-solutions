# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
    def __init__(self):
      self.leftSubtree = 0
      self.rightSubtree = 0
      self.foundX = False

    def subTreeCount(root):
      if root is None:
        return 0
      return 1+subTreeCount(root.left)+subTreeCount(root.right)

    def findXAndCountSubtreeNodes(root, x):
      if root:
        if root.val == x:
          leftSubtree = subTreeCount(root.left)
          rightSubtree = subTreeCount(root.right)

          return [leftSubtree, rightSubtree]
        else:
          value = findXAndCountSubtreeNodes(root.left, x)
          if value:
            return value

          return findXAndCountSubtreeNodes(root.right, x)

    leftSubtree, rightSubtree = findXAndCountSubtreeNodes(root, x)

    parentSubtree = n - leftSubtree - rightSubtree - 1
    nodesCapturedByY = max(leftSubtree, rightSubtree, parentSubtree)

    return nodesCapturedByY > n//2