import unittest


class MergeSort:

    @staticmethod
    def _merge(a, b):
        res = []
        while len(a) and len(b):
            next_elem = a.pop(0) if a[0] < b[0] else b.pop(0)
            res.append(next_elem)
        return res + a if len(a) else res + b if len(b) else res

    def _merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        left = self._merge_sort(arr[:len(arr)//2])
        right = self._merge_sort(arr[len(arr)//2:])
        return self._merge(left, right)

    def sort(self, arr):
        return self._merge_sort(arr)


class TestMergeSort(unittest.TestCase):

    _arrays = [[], [200], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [44, 4, -5, 0, 0, 4, 2, 1, 100, 101, 2]]

    def test_merge_sort(self):
        merge_sort = MergeSort()
        for array in self._arrays:
            expected = sorted(array.copy())
            self.assertEqual(merge_sort.sort(array), expected, "Error: {}".format(array))


if __name__ == '__main__':
    unittest.main()

