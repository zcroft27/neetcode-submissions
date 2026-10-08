# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0
        
        def dfs(node, max_so_far):
            if not node:
                return
            
            nonlocal good_nodes
            if node.val >= max_so_far:
                good_nodes += 1
            
            if node.left:
                dfs(node.left, max(max_so_far, node.val))
            if node.right:
                dfs(node.right, max(max_so_far, node.val))
            
        dfs(root, -101)
        return good_nodes