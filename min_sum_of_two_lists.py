import unittest


class MinSumOfTwoLists:
    @staticmethod
    def run(a, b):
        min_sum = float('inf')
        a.sort()
        b.sort()
        i = j = 0
        while i < len(a) and j < len(b):
            cur_sum = abs(a[i] - b[j])
            min_sum = min(min_sum, cur_sum)
            if a[i] > b[j]:
                j += 1
            else:
                i += 1
        return min_sum



class TestMinSumOfTwoLists(unittest.TestCase):

    _arrays = [([1], [2], 1),
               ([1, 2], [5, 3], 1),
               ([2, 1, 3, 6], [100, 67], 61)]

    def test_max_sum(self):
        for a, b, min_sum in self._arrays:
            self.assertEqual(MinSumOfTwoLists().run(a, b), min_sum, "Min sum of {} and {} should be: {}".format(a, b, min_sum))


if __name__ == '__main__':
    unittest.main()

