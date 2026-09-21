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

        def dfs(root): # returns [bool, int]
            if not root:
                return [True, 0]
            
            left_tree = dfs(root.left)
            right_tree = dfs(root.right)
            balanced = (
                left_tree[0] and
                right_tree[0] and
                abs(left_tree[1] - right_tree[1]) < 2
                )

            return [balanced, 1 + max(left_tree[1], right_tree[1])]
        
        return dfs(root)[0]