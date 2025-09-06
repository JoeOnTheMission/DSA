# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        now = head 
        seen = []
        while now:
            seen.append(now.val)
            now = now.next  
        now = head
        i = -1   
        while now:
            if now.val != seen[i]:
                return False
            i -= 1
            now = now.next
        return True 