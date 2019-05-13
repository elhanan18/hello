import unittest


class Allocator:
    def __init__(self, size):
        self._stack = list(range(0, size))

    def allocate(self):
        return self._stack.pop() if self._stack else -1

    def release(self, uid):
        self._stack.append(uid)


class TestAllocator(unittest.TestCase):

    def test_allocate(self):
        size = 100
        allocator = Allocator(size)
        for i in range(size):
            self.assertEqual(allocator.allocate(), size - 1 - i, "Allocate error")
        self.assertEqual(allocator.allocate(), -1, "Allocate error")
        for i in range(100):
            allocator.release(i)
        self.assertEqual(allocator.allocate(), 99, "Allocate error")


if __name__ == '__main__':
    unittest.main()
