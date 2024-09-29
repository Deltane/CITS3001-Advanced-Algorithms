#! /usr/bin/env python3

def max_sum_subarray_naive(xs: list[int]) -> int:
    best = 0  # Can always take empty subarray
    # Try every candidate xs[lwr:upr]
    for lwr in range(len(xs)):
        for upr in range(lwr + 1, len(xs) + 1):
            # Add up the candidate
            total = 0
            for i in range(lwr, upr):
                total += xs[i]
            # Keep track of the best
            best = max(best, total)
    return best


def max_sum_subarray_better(xs: list[int]) -> int:
    best = 0
    for lwr in range(len(xs)):
        total = 0
        # Incrementally grow subarray
        for i in range(lwr, len(xs)):
            total += xs[i]
            best = max(best, total)
    return best


def main():
    xs = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f'xs = {xs}')
    result = max_sum_subarray_naive(xs)
    print(f'max_sum_subarray_naive(xs) = {result}')
    result = max_sum_subarray_better(xs)
    print(f'max_sum_subarray_better(xs) = {result}')


if __name__ == '__main__':
    main()
