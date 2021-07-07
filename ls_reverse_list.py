"""Reverse linked list, leetcode 2"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Method 1: multiple assignment and iterative
class Solution(object):
    def reverse_list(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev

# Method 2: recursive function
class Solution(object):
    def reverse_list(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def reverse(node: ListNode, prev: ListNone = None):
            if not node:
                return node
            next, node.next = node.next, prev
            return reverse(next, prev)

        return reverse(head)
