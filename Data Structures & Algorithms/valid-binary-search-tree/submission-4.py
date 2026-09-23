# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, upper, lower):
            if not root:
                return True
            
            if root.val >= upper or root.val <= lower:
                return False
            
            left,right = True, True
            if root.left:
                left = dfs(root.left, root.val, lower)
            if root.right:
                right = dfs(root.right, upper, root.val)
            
            return left and right
        return dfs(root, float('inf'), float('-inf'))
