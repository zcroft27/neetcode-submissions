# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # DFS:
        # at each node, are my children (or me)
        # the sameTree as subroot
        # take the union of these

        def sameTree(q, p):
            if not q or not p:
                if q != p:
                    return False
                return True
            
            if q.val != p.val:
                return False
            return (
                sameTree(q.left, p.left) and
                sameTree(q.right, p.right)
            )
        
        def dfs(rt, subtree):
            if not rt:
                return subtree == None
            
            stack = [rt]
            while stack:
                curr = stack.pop()
                if (
                    sameTree(curr, subtree) or
                    sameTree(curr.left, subtree) or
                    sameTree(curr.right, subtree)
                ):
                    return True
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)

            return False
        return dfs(root, subRoot)
