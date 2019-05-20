import unittest


class Node:
    def __init__(self, val, next_node):
        self.val, self.next_node = val, next_node


class LinkedList:
    def __init__(self, arr):
        self.head = prev = None
        for n in arr:
            node = Node(n, None)
            if prev:
                prev.next_node = node
            else:
                self.head = node
            prev = node


class ReverseLinkedList:
    @staticmethod
    def iterative(head):
        prev = head
        cur = head.next_node
        while cur:
            next_node = cur.next_node
            cur.next_node = prev
            prev = cur
            cur = next_node
        return prev

    def recursive(self, head):
        if not head or not head.next_node:
            return head
        res = self.recursive(head.next_node)
        head.next_node.next_node = head
        head.next_node = None
        return res


class TestReverseLinkedList(unittest.TestCase):
    @staticmethod
    def _is_equal(a, b):
        while a and b:
            if a.val != b.val:
                return False
            a, b = a.next_node, b.next_node
        return True

    def setUp(self):
        self._a_head = LinkedList([1, 2, 3, 4]).head
        self._b_head = LinkedList([4, 3, 2, 1]).head

    def test_reverse_iterative(self):
        self.assertTrue(self._is_equal(ReverseLinkedList().iterative(self._a_head), self._b_head))

    def test_reverse_recursive(self):
        self.assertTrue(self._is_equal(ReverseLinkedList().recursive(self._a_head), self._b_head))


if __name__ == '__main__':
    unittest.main()
