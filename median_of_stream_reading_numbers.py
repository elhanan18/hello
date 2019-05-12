import unittest
import heapq


class FindMedian:
    def __init__(self):
        self._smaller_heap = []  # max heap
        self._bigger_heap = []
        heapq.heapify(self._smaller_heap)
        heapq.heapify(self._bigger_heap)

    def get_median(self, new_num):
        if len(self._smaller_heap) == 0:
            heapq.heappush(self._smaller_heap, -new_num)
        elif len(self._bigger_heap) == 0:
            if new_num < -self._smaller_heap[0]:
                heapq.heappush(self._smaller_heap, -new_num)
                self._balance_heaps()
            else:
                heapq.heappush(self._bigger_heap, new_num)
        else:
            if new_num > self._bigger_heap[0]:
                heapq.heappush(self._bigger_heap, new_num)
            else:
                heapq.heappush(self._smaller_heap, -new_num)
            self._balance_heaps()

        if len(self._smaller_heap) == len(self._bigger_heap):
            return (-self._smaller_heap[0] + self._bigger_heap[0]) / 2
        else:
            return -self._smaller_heap[0] if len(self._smaller_heap) > len(self._bigger_heap) else self._bigger_heap[0]

    def _balance_heaps(self):
        if len(self._smaller_heap) == len(self._bigger_heap) + 2:
            heapq.heappush(self._bigger_heap, -heapq.heappop(self._smaller_heap))
        elif len(self._bigger_heap) == len(self._smaller_heap) + 2:
            heapq.heappush(self._smaller_heap, -heapq.heappop(self._bigger_heap))


class TestFindMedian(unittest.TestCase):
    _input = [5, 15, 1, 3]
    _output = [5, 10, 5, 4]

    def test_merge_sort(self):
        find_median_handler = FindMedian()
        for i in range(len(self._input)):
            self.assertEqual(find_median_handler.get_median(self._input[i]), self._output[i], "Error")


if __name__ == '__main__':
    unittest.main()

