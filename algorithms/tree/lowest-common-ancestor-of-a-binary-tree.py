class Solution:

  def __init__(self):
    self.lca = None

  def lowestCommonAncestor(self, root, p, q):
    def traverse(node):
      # If reached the end of a branch, return False.
      if not node:
          return False

      # Left Recursion
      left = traverse(node.left)

      # Right Recursion
      right = traverse(node.right)

      # If the current node is one of p or q
      mid = node == p or node == q

      # If any two of the three flags left, right or mid become True.
      if mid + left + right >= 2:
          self.lca = node

      # Return True if either of the three bool values is True.
      return mid or left or right

    traverse(root)
    return self.lca
