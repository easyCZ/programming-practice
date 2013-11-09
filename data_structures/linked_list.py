
class Node:

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
        self.length = 0

    def __increment(self):
        self.length += 1

    def __decrement(self):
        self.length -= 1 if self.length > 0 else None

    def add_first(self, node):
        node.next = self.head
        self.head = node
        self.__increment()

    def add(self, node):
        if self.length == 0:
            self.head = node
            self.__increment()
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = node
            self.__increment()
            if self.length == 1:
                self.head = node

    def add_from_list(self, node_list):
        for node in node_list:
            self.add(node)
