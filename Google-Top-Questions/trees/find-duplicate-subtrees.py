# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
    count = collections.Counter()
    ans = []

    def serialized(root):
      nonlocal ans
      if root is None:
        return '#'
      serial = "{},{},{}".format(root.val, serialized(root.left), serialized(root.right))
      count[serial] += 1
      if count[serial] == 2:
        ans.append(root)

      return serial

    serialized(root)
    return ans