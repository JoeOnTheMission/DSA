# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        now = head 
        i = 1 
        l = now
        last = now
        new = ListNode(None) 
        while now:  
            if i % 2 != 0 and i != 1:
                m = now 
                mn = now.next
                temp = l.next
                l.next = m
                m.next = temp
                last.next = mn
                l = l.next 
                now = mn
            else:
                last = now
                now = now.next
                
            i += 1
        return head             
            