# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen_in_a = set()
        seen_in_b = set() 
        a = headA
        b = headB
        while a:
            seen_in_a.add(id(a))
            a = a.next
        while b:
            if id(b) in seen_in_a:
                return b
            b = b.next 
        
        return 