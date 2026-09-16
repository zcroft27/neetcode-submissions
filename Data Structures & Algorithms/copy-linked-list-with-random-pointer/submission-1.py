"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Iterate over the list, making new nodes.
        # Retain old random pointers.
        # Iterate over list again, for each next and random pointer,
        # look at map from old ID to new node.
        if not head:
            return None
        old_id_to_new_node = {}
        curr = head
        while curr:
            new_node = Node(curr.val, curr.next, curr.random)
            old_id_to_new_node[id(curr)] = new_node
            curr = curr.next
        
        curr = head
        while curr:
            new_node = old_id_to_new_node[id(curr)]
            if new_node.next is not None:
                new_node.next = old_id_to_new_node[id(curr.next)]
            else:
                new_node.next = None
            if new_node.random is not None:
                new_node.random = old_id_to_new_node[id(curr.random)]
            else:
                new_node.random = None
            curr = curr.next

        return old_id_to_new_node[id(head)]