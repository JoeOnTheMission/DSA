# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        check = head
        d = defaultdict(int)
        while slow:
            d[(slow.val,slow.next.val if slow.next else None)] += 1
            slow = slow.next
         
            if 3 in set(d.values()):
                while check:
                    if d[(check.val,check.next.val)] > 1:
                        return check            
                    check = check.next   
                

        return #is not cycle

