# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        carry = 0
        while l1 or l2:
            if l1 and l2:
                res = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif l1:
                res = l1.val + carry
                l1 = l1.next
            else: 
                res = l2.val + carry
                l2 = l2.next
            carry = res//10
            newNode = ListNode(res%10)
            curr.next = newNode
            curr = curr.next
        if carry!=0:
            newNode = ListNode(carry)
            curr.next = newNode
            curr = curr.next
        return head.next 