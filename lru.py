import unittest


class Node:
    def __init__(self, val, prev, next_):
        self.val, self.prev, self.next_ = val, prev, next_


class Item:
    def __init__(self, key, val):
        self.key, self.val = key, val


class LRU:
    def __init__(self, max_size):
        self._hash = {}
        self._count = 0
        self._max_size = max_size
        self._head = None
        self._last = None

    def get(self, key):
        return self._hash[key].val.val if key in self._hash else None

    def put(self, key, val):
        if key in self._hash:
            self._remove_item(key) if self._hash[key] != self._last else self._remove_last()
        elif self._count == self._max_size:
            self._remove_last()
        else:
            self._count += 1
        new_item = Item(key, val)
        if self._head:
            node = Node(new_item, None, self._head)
            node.next_.prev = self._head = node
        else:
            self._head = self._last = node = Node(new_item, None, None)
        self._hash[key] = node
        self._print_cache_values()

    def _remove_last(self):
        self._hash.pop(self._last.val.key, None)
        self._last = self._last.prev
        if self._last:
            self._last.next_ = None

    def _remove_item(self, key):
        if self._hash[key].prev:
            self._hash[key].prev.next_ = self._hash[key].next_
            self._hash[key].next_.prev = self._hash[key].prev
        self._hash.pop(key, None)

    def _print_cache_values(self):
        res = []
        next_item = self._head
        while next_item:
            res.append(next_item.val.val)
            next_item = next_item.next_
        print(res)


class TestLRU(unittest.TestCase):
    def setUp(self):
        self._lru = LRU(4)

    def test_lru(self):
        self._lru.put(1, 'a')
        self.assertEqual(self._lru.get(1), 'a')
        self._lru.put(2, 'b')
        self._lru.put(3, 'c')
        self._lru.put(4, 'd')
        self._lru.put(5, 'e')
        self.assertEqual(self._lru.get(1), None)
        self.assertEqual(self._lru.get(2), 'b')
        self.assertEqual(self._lru.get(5), 'e')
        self._lru.put(4, 'd')
        self._lru.put(6, 'f')
        self._lru.put(7, 'g')
        self.assertEqual(self._lru.get(5), 'e')
        self._lru.put(8, 'h')
        self.assertEqual(self._lru.get(5), None)
        self.assertEqual(self._lru.get(4), 'd')
        self.assertEqual(self._lru.get(6), 'f')


if __name__ == '__main__':
    unittest.main()

