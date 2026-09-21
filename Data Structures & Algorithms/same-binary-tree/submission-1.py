# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # BFS
        if not p or not q:
            if p == q:
                return True
            return False
        
        qp = deque([p])
        qq = deque([q])
        while qp and qq:
            curr_p = qp.popleft()
            curr_q = qq.popleft()
            
            if not curr_p or not curr_q:
                if curr_p != curr_q:
                    return False
                continue
            
            if curr_p.val != curr_q.val:
                return False

            qp.append(curr_p.left)
            qp.append(curr_p.right)
            qq.append(curr_q.left)
            qq.append(curr_q.right)
        
        if qp or qq:
            return False
        
        return True