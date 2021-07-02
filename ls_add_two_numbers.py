"""Add two numbers, leetcode 2"""
class Solution(object):
    """Method 1: Convert data type"""
    def reverse_num(self, node):
        """
        node: ListNode
        return: int
        """
        num = ''
        while node:
            value, node = node.val, node.next
            num += str(value)

        return int(num[::-1])

    def to_linked_list(self, str_num):
        """
        type num: str
        return: LintNode
        """
        prev = None
        for digit in str_num:
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
        str_num = str(self.reverse_num(linked_list_1) + \
            self.reverse_num(linked_list_2))

        return self.to_linked_list(str_num)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
