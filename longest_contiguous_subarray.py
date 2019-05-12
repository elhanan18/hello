import unittest


class LongestIncreasingSubarray:
    @staticmethod
    def run(arr):
        max_size = cur_size = 0 if not arr else 1
        for i in range(1, len(arr)):
            cur_size = cur_size + 1 if arr[i] > arr[i-1] else 1
            max_size = max(cur_size, max_size)
        return max_size


class TestLongestIncreasingSubarray(unittest.TestCase):

    _arrays = [([], 0), ([0], 1), ([1, -1], 1), ([-1, 1], 2), ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 2),
               ([-2, -1, -3, -6], 2), ([-1, -2, -3], 1), ([-1, -2, 8], 2), ([1, 2, 3], 3),
               ([5, 6, 3, 5, 7, 8, 9, 1, 2], 5), ([12, 13, 1, 5, 4, 7, 8, 10, 10, 11], 4)]

    def test_max_sum(self):
        for arr, longest in self._arrays:
            self.assertEqual(LongestIncreasingSubarray().run(arr), longest, "Longest subarray size of {} should be: {}".
                             format(arr, longest))


if __name__ == '__main__':
    unittest.main()

