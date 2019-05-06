import unittest


class CountSetBits:
    _lookup_table = {0: 0, 1: 1, 2: 1, 3: 2}
    _mask = 0x3
    _mask_size = 2

    def run(self, n):
        res = 0
        for i in range(32//self._mask_size):
            key = (n >> (i * self._mask_size)) & self._mask
            res += self._lookup_table[key]
        return res


class TestCountSetBits(unittest.TestCase):
    _num = {0: 0, 1: 1, 2: 1, 3: 2, 4: 1, 100: 3, 4294967295: 32}

    def test_count_set_bits(self):
        count_set_bits = CountSetBits()
        for n, num_of_bits in self._num.items():
            self.assertEquals(count_set_bits.run(n), num_of_bits, "Result for {} should be {}".format(n, num_of_bits))


if __name__ == '__main__':
    unittest.main()

