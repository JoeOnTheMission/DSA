# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        now = head
        while now:
            nxt = now.next 
                                  
            while nxt and now.val == nxt.val:#nxt is the next unique
                nxt = nxt.next               
            now.next = nxt
            now = now.next 
        return head
            

            