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


# BT DFS
class DFS:
    def __init__(self):
        self._visited = set()
        self._res = []

    def run(self, root):
        if root:
            self._visited.add(root)
            self._res.append(root.val)
            self.run(root.left)
            self.run(root.right)

        return self._res


class TestBFS_DFS(unittest.TestCase):
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

    _bfs_expected = [2, 7, 5, 2, 6, 9, 5, 11, 4]
    _dfs_expected = [2, 7, 2, 6, 5, 11, 5, 9, 4]

    def test_bfs(self):
        self.assertEqual(BFS().run(self._tree), self._bfs_expected, "Error")

    def test_dfs(self):
        self.assertEqual(DFS().run(self._tree), self._dfs_expected, "Error")


if __name__ == '__main__':
    unittest.main()

