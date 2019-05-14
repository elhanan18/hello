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


class InsertionSort:
    @staticmethod
    def sort(arr):
        if len(arr) < 2:
            return arr
        for i in range(1, len(arr)):
            while i > 0 and arr[i-1] > arr[i]:
                arr[i], arr[i-1] = arr[i-1], arr[i]  # replace
                i -= 1
        return arr


class BubbleSort:
    @staticmethod
    def sort(arr):
        for i in range(len(arr) - 1):
            swapped = False
            for j in range(len(arr) - 1 - i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]  # replace
                    swapped = True
            if not swapped:
                break
        return arr


class TestSort(unittest.TestCase):

    _arrays = [[], [200], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [44, 4, -5, 0, 0, 4, 2, 1, 100, 101, 2]]

    def test_sort(self):
        for array in self._arrays:
            expected = sorted(array.copy())
            self.assertEqual(MergeSort().sort(array.copy()), expected, "Error - Merge Sort: {}".format(array))
            self.assertEqual(InsertionSort().sort(array.copy()), expected, "Error - Insertion Sort: {}".format(array))
            self.assertEqual(BubbleSort().sort(array.copy()), expected, "Error - Bubble Sort: {}".format(array))


if __name__ == '__main__':
    unittest.main()

