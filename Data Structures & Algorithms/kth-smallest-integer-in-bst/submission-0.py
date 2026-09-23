# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        def dfs(root):
            if not root:
                return
            if len(heap) >= k:
                heapq.heappush(heap, -1*root.val)
                heapq.heappop(heap)
            else:
                heapq.heappush(heap, -1*root.val)
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
        
        dfs(root)
        return -1*heapq.heappop(heap)