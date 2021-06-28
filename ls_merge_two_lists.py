"""Merge two lists, leetcode 21"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def merge_two_lists(self, list1, list2):
        """
        :type list1: ListNode
        :type list2: ListNode
        :rtype: ListNode
        """
        # Swap
        if not list1 or list2 and list1.val > list2.val:
            list1, list2 = list2, list1
        # Recursion
        if list1:
            list1.next = self.merge_two_lists(list1.next, list2)

        return list1
