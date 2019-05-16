import unittest


class FindFibSum:
    @staticmethod
    def run(n):
        n_1 = 0
        n_2 = 1
        sum_fib = 2
        for i in range(n - 2):
            tmp = n_1
            n_1 = n_2
            n_2 = tmp + n_1
            sum_fib = sum_fib + n_1 + n_2
        return n_1 if n == 0 else n_2 if n == 1 else sum_fib

    # def calc(self, n):
    #     if n == 0:
    #         return 0
    #     elif n == 1:
    #         return 1
    #     return fib(n) + self.calc(n-1)


class TestFindFibNum(unittest.TestCase):

    # _fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    _fib = [0, 1, 2, 4, 7, 12, 20, 33, 54, 88]

    def test_find_fib_num(self):
        for i in range(len(self._fib)):
            self.assertEqual(FindFibSum().run(i), self._fib[i], "Fib sum {} should be: {}".format(i, self._fib[i]))


if __name__ == '__main__':
    unittest.main()

