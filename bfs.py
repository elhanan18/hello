import unittest


class Node:
    def __init__(self, val, left, right):
        self.val, self.left, self.right = val, left, right


# BT BFS
class BFS:
    @staticmethod
    def run(root):
        queue = []
        res = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            if node:
                res.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        return res


class TestBFS(unittest.TestCase):
    # https://en.wikipedia.org/wiki/Binary_tree#/media/File:Binary_tree.svg
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

    _expected = [2, 7, 5, 2, 6, 9, 5, 11, 4]

    def test_bfs(self):
        self.assertEqual(BFS().run(self._tree), self._expected, "Error")


if __name__ == '__main__':
    unittest.main()

