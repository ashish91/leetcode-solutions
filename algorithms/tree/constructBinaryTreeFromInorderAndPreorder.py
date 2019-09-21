# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            inorderIndex = inorder.index(preorder.pop(0))
            curr = TreeNode(inorder[inorderIndex])
            
            curr.left = self.buildTree(preorder, inorder[0:inorderIndex])
            curr.right = self.buildTree(preorder, inorder[inorderIndex+1:])
            
            return curr
        return None
