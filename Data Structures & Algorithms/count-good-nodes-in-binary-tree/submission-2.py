# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0
        
        q = deque()
        q.append([root, float('-inf')])
        while q:
            curr, maxSoFar = q.popleft()
            if curr.val >= maxSoFar:
                good_nodes += 1
            maxSoFar = max(maxSoFar, curr.val)
            if curr.left:
                q.append([curr.left, maxSoFar])
            if curr.right:
                q.append([curr.right, maxSoFar])
        
        return good_nodes
            