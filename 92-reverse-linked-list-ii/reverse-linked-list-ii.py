# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev, cur = dummy, head
        pos = 1
        while pos < left:
            prev = cur 
            cur= cur.next
            pos += 1

        left_prev = prev
        l = cur
        prev = None
        while pos <= right:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            pos += 1
        left_prev.next = prev
        l.next = cur
        return dummy.next