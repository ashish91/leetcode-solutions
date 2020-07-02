# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        todel = list(to_delete)
        a = []

        if root.val not in todel:
            a.append(root)

        self.dfs(root,todel,a)

        return a

    def dfs(self,t,d,a):
        if not t:
            return None

        t.left = self.dfs(t.left,d,a)
        t.right = self.dfs(t.right,d,a)

        if t.val in d:
            if t.left:
                a.append(t.left)
            if t.right:
                a.append(t.right)

            return None

        return t
