# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0
        def dfs(root, max_seen):
            nonlocal good_nodes
            if not root:
                return 0
            if root.val >= max_seen:
                good_nodes += 1
            max_seen = max(max_seen, root.val)
            if root.left:
                left = dfs(root.left, max_seen)
            if root.right:
                right = dfs(root.right, max_seen)
            
        dfs(root, root.val)
        return good_nodes
            