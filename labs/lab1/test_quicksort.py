#! /usr/bin/env python3

import unittest

from quicksort import *

from random import Random

SEED = 3001
RUNS = 100
SIZE = 1000
RANGE = 1000


class TestQuicksort(unittest.TestCase):
    def test_quicksort(self):
        random = Random(SEED)
        for i in range(RUNS):
            seed = random.getrandbits(64)
            random = Random(seed)
            xs = [random.randint(0, RANGE) for _ in range(SIZE)]
            expected = sorted(xs.copy())
            received = quicksort(xs.copy())
            msg = f'quicksort failed on run {i} with seed={seed}'
            self.assertEqual(received, expected, msg=msg)


if __name__ == '__main__':
    unittest.main()
