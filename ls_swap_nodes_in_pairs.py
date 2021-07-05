"""Swap nodes in pairs, leetcode 24"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Method 1
# 현업에서는 복잡한 구조로 구성되어 단순히 자료의 값만 바꾸는 방법은 실용성이 떨어진다.
class Solution(object):
    def swap_pairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        node = head

        while node and node.next:

            node.val, node.next.val = node.next.val, node.val
            node = node.next.next

        return head

# Method 2
class Solution(object):
    def swap_pairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        node = prev =ListNode(None)
        prev.next = head

        while head and head.next:
            # Swap pairs
            temp = head.next
            head.next = temp.next
            temp.next = head

            # Save swaped pairs
            prev.next = temp

            # Move the next
            head = head.next
            prev = prev.next.next

        return node.next
