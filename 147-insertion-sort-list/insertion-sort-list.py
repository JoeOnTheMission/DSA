# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        now = head
        sorted_list = []
        new = ListNode(None)
        new_head = new
        
        while now:
            num_to_insert = now.val
            sorted_list.append(num_to_insert)
            i = len(sorted_list) - 1
            #find its place in list
            while i > 0 and sorted_list[i - 1] >= sorted_list[i]:
                sorted_list[i], sorted_list[i - 1] = sorted_list[i - 1], sorted_list[i]
                i -= 1
            now = now.next
      
        for num in sorted_list:
            new.next =  ListNode(num)
            new = new.next
        return new_head.next
        
            