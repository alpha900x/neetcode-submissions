# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        head = ListNode()
        c = 0
        curr = head
        while curr1 or curr2 or c: 
            if  curr1==None and curr2==None:
                d = c
                c = 0
            elif curr2==None:
                d = (curr1.val+c)%10 
                c = (curr1.val+c)//10
                curr1 = curr1.next
            elif curr1==None:
                d = (curr2.val+c)%10
                c = (curr2.val+c)//10
                curr2 = curr2.next
            else:
                d = (curr1.val+curr2.val+c)%10
                c = (curr1.val+curr2.val+c)//10
                curr1 = curr1.next
                curr2 = curr2.next
            curr.next = ListNode(d)  
            curr = curr.next 
        return head.next
            
            
