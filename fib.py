import unittest


class FindFibNum:
    def find_recursive(self, n):
        return 0 if n == 0 else 1 if n == 1 else self.find_recursive(n-1) + self.find_recursive(n-2)

    @staticmethod
    def find_iteration(n):
        n_1 = 0
        n_2 = 1
        for i in range(n - 2):
            tmp = n_1
            n_1 = n_2
            n_2 = tmp + n_1
        return n_1 if n == 0 else n_2 if n == 1 else n_1 + n_2

    _memory = {}

    def find_recursive_with_memory(self, n):
        if n in self._memory:
            return self._memory[n]
        if n == 0:
            res = 0
        elif n == 1:
            res = 1
        else:
            res = self.find_recursive_with_memory(n-1) + self.find_recursive_with_memory(n-2)
        self._memory[n] = res
        return res


class TestFindFibNum(unittest.TestCase):

    _fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    _find_fib_num = FindFibNum()
    _methods = [_find_fib_num.find_recursive, _find_fib_num.find_iteration, _find_fib_num.find_recursive_with_memory]

    def test_find_fib_num(self):
        for method in self._methods:
            for i in range(len(self._fib)):
                self.assertEqual(method(i), self._fib[i], "Fib number {} should be: {}".format(i, self._fib[i]))


if __name__ == '__main__':
    unittest.main()

