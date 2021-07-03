"""Add two numbers, leetcode 2"""

# Method 1
import functools

class Solution(object):
    """Method 1: Convert data type"""
    def reverse_num(self, node):
        """
        node: ListNode
        return: int
        """
        digits = []
        while node:
            digit, node = node.val, node.next
            digits.append(digit)

        num = functools.reduce(lambda x, y : 10 * x + y, digits[::-1], 0)

        return num

    def to_linked_list(self, num):
        """
        type num: str
        return: LintNode
        """
        prev = None
        for digit in str(num):
            node = ListNode(digit)
            node.next = prev
            prev = node

        return node

    def add_two_numbers(self, linked_list_1, linked_list_2):
        """
        linked_list_1: ListNode
        linked_list_2: ListNode
        return: ListNode
        """
        num = self.reverse_num(linked_list_1) + \
            self.reverse_num(linked_list_2)

        return self.to_linked_list(num)

# Method 2
class Solution(object):
    """Method 2: Full adder"""
    def add_two_numbers(self, linked_list_1, linked_list_2):
        """
        :type linked_list_1: ListNode
        :type linked_list_2: ListNode
        :rtype: ListNode
        """

        head = root = ListNode(0)
        carry = 0

        while linked_list_1 or linked_list_2 or carry:
            SUM = 0

            if linked_list_1:
                SUM += linked_list_1.val
                linked_list_1 = linked_list_1.next

            if linked_list_2:
                SUM += linked_list_2.val
                linked_list_2 = linked_list_2.next

            carry, val = divmod(SUM + carry, 10)
            head.next = ListNode(val)
            head = head.next

        return root.next
