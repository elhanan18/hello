import unittest


class Node:
    def __init__(self, val, left, right):
        self.val, self.left, self.right = val, left, right


class BTSerialization:

    def _insert_node(self, node, idx, res):
        if node:
            res[idx] = node.val
            self._insert_node(node.left, 2 * idx + 1, res)
            self._insert_node(node.right, 2 * idx + 2, res)

    def _get_node(self, idx, idx_val_map):
        if idx not in idx_val_map:
            return None
        return Node(idx_val_map[idx], self._get_node(idx * 2 + 1, idx_val_map), self._get_node(idx * 2 + 2, idx_val_map))

    def serialize(self, root):
        res = {}
        self._insert_node(root, 0, res)
        return res

    def deserialize(self, idx_val_map):
        if 0 in idx_val_map:
            return Node(idx_val_map[0], self._get_node(1, idx_val_map), self._get_node(2, idx_val_map))


class TestBTSerialization(unittest.TestCase):
    # https: // en.wikipedia.org / wiki / Binary_tree  # /media/File:Binary_tree.svg
    _tree = Node(2,
                 Node(7,
                      Node(2, None, None),
                      Node(6,
                           Node(5, None, None),
                           Node(11, None, None))),
                 Node(5,
                      None,
                      Node(9,
                           Node(4, None, None),
                           None)))

    _map = {0: 2, 1: 7, 2: 5, 3: 2, 4: 6, 6: 9, 9: 5, 10: 11, 13: 4}

    def _identical_trees(self, a, b):
        if a is None and b is None:
            return True

        if a is not None and b is not None:
            return (a.val == b.val and
                    self._identical_trees(a.left, b.left) and
                    self._identical_trees(a.right, b.right))

    def test_serialize(self):
        self.assertEqual(BTSerialization().serialize(self._tree), self._map, "serialize error")
        is_identical = self._identical_trees(BTSerialization().deserialize(self._map), self._tree)
        self.assertTrue(is_identical, "deserialize error")


if __name__ == '__main__':
    unittest.main()

