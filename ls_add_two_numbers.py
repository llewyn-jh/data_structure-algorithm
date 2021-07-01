"""Add two numbers, leetcode 2"""
class Solution(object):

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
