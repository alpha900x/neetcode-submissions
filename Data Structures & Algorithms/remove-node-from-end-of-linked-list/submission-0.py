# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        prev = head
        while n>0:
            n-=1
            fast = fast.next
        
        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next
        
        prev.next = slow.next
        print(slow.val,prev.val,fast)
        if prev == slow:
            return prev.next
        return head

        
        
        
