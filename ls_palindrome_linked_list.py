"""Palindrome linked list, #234, level 1
A script won't be able to run. Use only it for a reference."""

def is_palindrome_v1(head) -> bool:
    """Use slicing"""

    pal = []
    node = head
    # Change a linked list for a list
    while node is not None:
        pal.append(node.val)
        node = node.next

    # Use slicing
    return pal == pal[::-1]

def is_palindrome_v2(head) -> bool:
    """Use the runner method"""

    # Create a reversed linked list by using the runner method
    fast = slow = head
    rev = None
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next

    # When a list is an even
    if fast:
        slow = slow.next

    # Check out a palindrome
    while rev and rev.val == slow.val:
        rev = rev.next
        slow = slow.next

    return not rev
