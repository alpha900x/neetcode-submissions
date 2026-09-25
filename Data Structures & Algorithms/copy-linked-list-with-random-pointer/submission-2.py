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
        if head == None:
            return None
        copy = Node(head.val)
        ccurr = copy
        ocurr = head

        while ocurr:    
            ocurr = ocurr.next
            if ocurr:
                newNode = Node(ocurr.val)
                ccurr.next = newNode
                ccurr = ccurr.next
            
        h = {}
        ocurr = head
        ccurr = copy
        while ocurr:
            h[ocurr] = ccurr
            ocurr = ocurr.next
            ccurr = ccurr.next
        
        ccurr = copy
        ocurr = head
        while ocurr:
            if ocurr.random:
                ccurr.random = h[ocurr.random]
            ccurr = ccurr.next
            ocurr = ocurr.next

        return copy