#! /usr/bin/env python3

# fmt: off
import sys
import os
sys.path.append(os.path.abspath('../../lecture02_sorting/code'))

import random
import timeit
from collections import defaultdict
from statistics import mean, median, stdev

from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quicksort import quicksort
# fmt: on

SORTING_ALGS = {
    "insertion_sort": insertion_sort,
    "merge_sort": merge_sort,
    "quicksort": quicksort,
}

SIZE = 1000
RANGE = 1000
RUNS = 100
SAMPLES = 5


def benchmark_sorting():
    times = defaultdict(list)
    for run_id in range(RUNS):
        xs = [random.randint(0, RANGE) for _ in range(SIZE)]
        for name, alg in SORTING_ALGS.items():
            time = timeit.timeit(lambda: alg(xs.copy()), number=SAMPLES)
            times[name].append(time)
    return times


def print_stats(times):
    print(f'Time to sort {SIZE} random ints:')
    for name, ts in times.items():
        print(name)
        print(f'\tminimum:      {min(ts):.6f} s')
        print(f'\tmedian:       {median(ts):.6f} s')
        print(f'\tmaximum:      {max(ts):.6f} s')
        print(f'\tmean ± stdev: {mean(ts):.6f} ± {stdev(ts):.6f} s')


def main():
    print_stats(benchmark_sorting())


if __name__ == '__main__':
    main()
