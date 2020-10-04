# DFS + BFS
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
    def dfs(node, parent=None):
      if node:
        node.parent = parent
        dfs(node.left, node)
        dfs(node.right, node)

    dfs(root)
    queue = [[target, 0]]
    visited = {target: True}
    while len(queue) > 0:
      if queue[0][1] == K:
        return [node.val for node, d in queue]

      curr, d = queue.pop(0)
      neighbours = [curr.left, curr.right, curr.parent]

      for nei in neighbours:
        if nei and not nei in visited:
          visited[nei] = True
          queue.append([nei, d+1])

    return []

# Double DFS
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
  def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
    ans = []
    def subtree_dfs(node, distance):
      if node is None:
        return

      if distance == K:
        ans.append(node.val)
        return

      subtree_dfs(node.left, distance+1)
      subtree_dfs(node.right, distance+1)

    def dfs(node):
      if node is None:
        return -1
      elif node is target:
        subtree_dfs(node, 0)
        return 1
      else:
        left, right = dfs(node.left), dfs(node.right)
        if left > 0:
          if left == K:
            ans.append(node.val)
          elif left < K:
            subtree_dfs(node.right, left+1)
          return left+1
        elif right > 0:
          if right == K:
            ans.append(node.val)
          elif right < K:
            subtree_dfs(node.left, right+1)
          return right+1
        else:
          return -1

    dfs(root)
    return ans