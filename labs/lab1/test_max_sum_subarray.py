#! /usr/bin/env python3

import unittest

from max_sum_subarray import *


class TextMaxSumSubarray(unittest.TestCase):
    def test_max_sum_subarray_naive(self):
        xs = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        expected = 6
        received = max_sum_subarray_naive(xs)
        self.assertEqual(received, expected)

    def test_max_sum_subarray_better(self):
        xs = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        expected = 6
        received = max_sum_subarray_better(xs)
        self.assertEqual(received, expected)


if __name__ == '__main__':
    unittest.main()
