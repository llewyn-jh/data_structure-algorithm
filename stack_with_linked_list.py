from _typeshed import Self


class Node:
    """Node: LinkedList"""
    def __init__(self, item, next) -> None:
        """Set initial item and next of a linked list"""
        self.item = item
        self.next = next

class Stack:
    """Last in first out"""
    def __init__(self) -> None:
        """Set an initial the next values in the class Node"""
        self.last = None

    def push(self, item):
        """Add an item"""
        self.last = Node(item, self.last)

    def pop(self):
        """Pop an item"""
        item = self.last.item
        self.last = self.last.next
        return item
