# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: 
            return []
        
        zigzag = []
        s1 = [root]
        s2 = []
        temp = s1
        leftToRight = True
        
        while s1:
            zigzag.append([])
            for i in range(len(s1)):
                curr = s1.pop()
                zigzag[-1].append(curr.val)
                
                if leftToRight:
                    if curr.left: s2.append(curr.left)
                    if curr.right: s2.append(curr.right)
                else:
                    if curr.right: s2.append(curr.right)
                    if curr.left: s2.append(curr.left)
            leftToRight = not leftToRight
            s1, s2 = s2, s1
            
        return zigzag