import unittest


class MaxSumContiguousSubarray:
    @staticmethod
    def run(arr):
        max_sum = cur_sum = 0 if not arr else arr[0]
        for n in arr[1:]:
            cur_sum = max(n, cur_sum + n)
            max_sum = max(max_sum, cur_sum)
        return max_sum


class TestMaxSumContiguousSubarray(unittest.TestCase):

    _arrays = [([], 0), ([0], 0), ([1, -1], 1), ([-1, 1], 1), ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
               ([-2, -1, -3, -6], -1), ([-1, -2, -3], -1), ([-1, -2, 8], 8)]

    def test_max_sum(self):
        for arr, max_sum in self._arrays:
            self.assertEqual(MaxSumContiguousSubarray().run(arr), max_sum, "Max sum of {} should be: {}".format(arr, max_sum))


if __name__ == '__main__':
    unittest.main()

