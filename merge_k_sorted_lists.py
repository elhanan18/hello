import unittest


class ListNode:
    def __init__(self, x, next_):
        self.val = x
        self.next = next_


class MergeKSortedLists:
    def _merge_lists(self, a, b):
        if len(a) + len(b) < 2:
            return a + b
        if len(a) + len(b) == 2:
            return a + b
        return self._m

    def run(self, lists_array):
        size = len(lists_array)
        if size == 1:
            return lists_array[0]
        if size == 0:
            return None
        return self._merge_lists(lists_array[:size//2], lists_array[size//2:])


class TestMergeKSortedLists(unittest.TestCase):
    _lists_array = [ListNode(1, ListNode(10, ListNode(20, None))),
                    ListNode(4, ListNode(11, ListNode(13, None))),
                    ListNode(3, ListNode(8, ListNode(9, None)))]

    _expected = [1, 3, 4, 8, 9, 10, 11, 13, 20]

    def test_merge(self):
        merge_lists = MergeKSortedLists()
        self.assertEqual(merge_lists.run([]), None, "Error")
        result = merge_lists.run(self._lists_array)
        result_array = []
        while result and result.next:
            result_array.append(result.val)
            result = result.next
        self.assertEqual(result_array, self._expected, "Error")


if __name__ == '__main__':
    unittest.main()

