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
        #space between fast and slow
        while n>0:
            n-=1
            fast = fast.next
        #make fast go to end (None)
        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next
        #replace prev next with slow's next
        prev.next = slow.next
        if prev == slow:
            # handles case where slow and next are same,ie, first element of list
            return prev.next
        return head

        
        
        
