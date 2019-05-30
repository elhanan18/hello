import unittest


class LongestIncreasingSubarray:
    @staticmethod
    def run(arr):
        tmp = [1] * len(arr)
        for i in range(len(arr)):
            for j in range(i):
                if arr[i] > arr[j]:
                    tmp[i] = max(tmp[j] + 1, tmp[i])
        return max(tmp) if tmp else 0


class TestLongestIncreasingSubarray(unittest.TestCase):

    _arrays = [([], 0),
               ([0], 1),
               ([1, -1], 1),
               ([-1, 1], 2),
               ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 4),
               ([-2, -1, -3, -6], 2),
               ([-1, -2, -3], 1), ([-1, -2, 8], 2),
               ([1, 2, 3], 3),
               ([5, 6, 3, 5, 7, 8, 9, 1, 100], 6)]

    def test_max_sum(self):
        for arr, longest in self._arrays:
            self.assertEqual(LongestIncreasingSubarray().run(arr), longest, "Longest subarray size of {} should be: {}".
                             format(arr, longest))


if __name__ == '__main__':
    unittest.main()

