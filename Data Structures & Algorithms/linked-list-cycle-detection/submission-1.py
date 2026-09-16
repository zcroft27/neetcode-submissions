# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        t = head    
        h = head
        while t and h and h.next:
            t = t.next
            h = h.next.next
            if t == h:
                return True
        return False