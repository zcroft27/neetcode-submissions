# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # BFS, therefore no call stack
        p_ancestors = set()
        parents = {root: None} # node to it's parent
        curr_parent = None
        queue = deque([root])
        while queue:
            if p in parents and q in parents:
                break
            curr = queue.popleft()
            if curr.left:
                parents[curr.left] = curr
                queue.append(curr.left)
            if curr.right:
                parents[curr.right] = curr
                queue.append(curr.right)
    
        while p:
            p_ancestors.add(p)
            p = parents[p]

        while q not in p_ancestors:
            q = parents[q]
        
        return q