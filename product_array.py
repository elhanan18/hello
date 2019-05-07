import unittest


class ProductArray:
    @staticmethod
    def run(arr):
        if not arr:
            return []
        n = len(arr)
        tmp_left = [1] * n
        tmp_right = [1] * n
        for i in range(n-1):
            tmp_left[i+1] = tmp_left[i] * arr[i]
            tmp_right[n-i-2] = tmp_right[n-i-1] * arr[n-i-1]
        return [tmp_left[i] * tmp_right[i] for i in range(n)]

        # without tmp array
        # n = len(arr)
        # res = [1] * n
        # for i in range(n-1):
        #     res[i+1] = res[i] * arr[i]
        # prod = 1
        # for i in range(n):
        #     res[n-i-1] *= prod
        #     prod *= arr[n-i-1]
        # return res


class TestProductArray(unittest.TestCase):

    _arrays = [([], []),
               ([10, 3, 5, 6, 2], [180, 600, 360, 300, 900]),
               ([10, 10], [10, 10])]

    def test_product_array(self):
        for input_arr, output_arr in self._arrays:
            self.assertEqual(ProductArray().run(input_arr), output_arr, "Output of {} should be: {}".format(input_arr, output_arr))


if __name__ == '__main__':
    unittest.main()

