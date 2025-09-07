# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        a,b = list1,list2
        
        new = ListNode(0)
        head = new
        while a or b:
            if a and b:#both exist 
                if a.val > b.val:   
                    new.next = b
                    b = b.next
                    
                else:
                    new.next = a
                    a = a.next

            elif  a and not b:# a exist but not b
                new.next = a
                a = a.next

            elif not a and b:# b exist but not a
                new.next = b
                b = b.next   
                
            new = new.next    
        return head.next