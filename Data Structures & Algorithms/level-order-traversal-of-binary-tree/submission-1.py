# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        worklist = deque([root])
        while worklist:
            wlen = len(worklist)
            level = []
            for _ in range(wlen):
                node = worklist.popleft()
                if node:
                    level.append(node.val)
                    worklist.append(node.left)
                    worklist.append(node.right)
            if level:
                res.append(level)
        
        return res