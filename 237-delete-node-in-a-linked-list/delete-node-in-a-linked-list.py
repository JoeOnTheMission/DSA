# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        now = node 
        while now.next:
            a = now.next.val
            now.val = a
            last = now 
            now = now.next
        last.next = None
        