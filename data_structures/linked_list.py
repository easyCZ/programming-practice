
class Node:
    """
    Common Node implementation for a LinkedList. Equality of value and to string are supported.
    """

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        """
        Check for equality. Only type and value are compared to avoid tail recursion
        and inherent False or infinite loop.
        """
        return isinstance(other, self.__class__) and other.value == self.value


class LinkedList:

    def __init__(self):
        self.head = None
        self.last = None
        self.length = 0

    def __increment(self):
        self.length += 1

    def __decrement(self):
        self.length -= 1 if self.length > 0 else None

    def add_first(self, node):
        """
        Add a node to the front of the LinkedList.
        """
        node.next = self.head
        self.head = node
        self.__increment()
        if self.length == 1:
            self.last = node

    def add(self, node):
        """
        Adds a Node to the tail.
        """
        if self.length == 0:
            self.head = self.last = node
        else:
            self.last.next = self.last = node
        self.__increment()

    def add_from_node_list(self, node_list):
        """
        Wrapper for adding elements from a list of Nodes.
        """
        for node in node_list:
            self.add(node)
