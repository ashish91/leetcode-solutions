# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def maximumAverageSubtree(self, root: TreeNode) -> float:
    def dfs(node):
      if node is None:
        return [0, 0, 0]

      left_max_avg, left_sum, left_count = 0, 0, 0
      if node.left is not None:
        left_max_avg, left_sum, left_count = dfs(node.left)

      right_max_avg, right_sum, right_count = 0, 0, 0
      if node.right is not None:
        right_max_avg, right_sum, right_count = dfs(node.right)

      sum = left_sum + right_sum + node.val
      count = left_count + right_count + 1

      curr_avg = (sum*1.00000/count)
      child_max_avg = max(left_max_avg, right_max_avg)
      max_avg = max(curr_avg, child_max_avg)

      return [ max_avg, sum, count ]

    return dfs(root)[0]
