import unittest
from linked_list import LinkedList, Node


class TestLinkedList(unittest.TestCase):

    def test_empty(self):
        llist = LinkedList()
        self.assertEqual(None, llist.head)
        self.assertEqual(0, llist.length)

    def test_add_length_incremented(self):
        llist = LinkedList()
        node = Node(1)
        llist.add(node)
        self.assertEqual(1, llist.length)

    def test_add_first_length_incremented(self):
        llist = LinkedList()
        node = Node(1)
        llist.add_first(node)
        self.assertEqual(1, llist.length)

    def test_add_adds_to_end(self):
        llist = LinkedList()
        node = Node(1)
        node2 = Node(2)
        llist.add(node)
        llist.add(node2)
        self.assertEqual(llist.head, node)

    def test_add_from_list(self):
        node_list = [Node(i) for i in range(10)]
        llist = LinkedList()
        llist.add_from_node_list(node_list)
        self.assertEqual(10, llist.length)


if __name__ == '__main__':
    unittest.main()
