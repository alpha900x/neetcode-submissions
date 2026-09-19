# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        nodes=[]
        while head!=None:
            nodes.append(head.val)
            head = head.next
        newHead = ListNode()
        curr = newHead
        for i in range(len(nodes)-1,-1,-1):
            newNode = ListNode(nodes[i],None)
            curr.next = newNode
            curr = curr.next
        return newHead.next


            

        