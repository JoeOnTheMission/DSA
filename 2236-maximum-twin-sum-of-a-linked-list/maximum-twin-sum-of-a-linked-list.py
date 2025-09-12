# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head
        slow = head
        res = float('-inf')
        store = []
        while fast:
            store.append(slow.val)
            fast = fast.next.next
            slow = slow.next
        i = -1
        while slow:
            twin = slow.val + store[i]
            res = max(res,twin)
            slow = slow.next
            i -= 1
        return res
        
