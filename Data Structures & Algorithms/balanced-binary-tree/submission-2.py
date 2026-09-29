# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        self.balanced = True

        def treeHeight(node):
            if not self.balanced:
                return 0
            
            if not node:
                return 0

            leftH = treeHeight(node.left) + 1
            rightH = treeHeight(node.right) + 1
            
            if abs(leftH-rightH)>1:
                self.balanced = False
            
            return max(leftH, rightH)
        
        treeHeight(root)
        return self.balanced



        
    