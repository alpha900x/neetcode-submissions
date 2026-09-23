# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
    #find middle using floyd two pointers
        slow = head
        fast = head
        while fast.next:
            if fast.next.next:
                fast = fast.next.next
            else:
                fast = fast.next
            slow = slow.next
        list1 = head
        list2 = slow.next
        slow.next = None
    #reverse list2
        curr = list2
        prev = None
        while curr:
            node = curr.next
            curr.next = prev
            prev = curr
            curr = node
        list2 = prev
    #interleave list1 and list2
        while list1 and list2:
            rlist = list1.next
            list1.next = list2
            list1 = rlist
            llist = list2.next
            list2.next = list1
            list2 = llist
    
    

        
        
        
