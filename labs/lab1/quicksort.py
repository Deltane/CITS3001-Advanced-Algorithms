#! /usr/bin/env python3

# Partitions xs[lwr:upr] by xs[upr-1] and returns index of the pivot
def partition(xs: list, lwr: int, upr: int) -> int:
    # Select last element as pivot
    pivot = xs[upr-1]
    # Scan over list and swap any element <= pivot down
    mid = lwr
    for i in range(lwr, upr):
        if xs[i] <= pivot:
            xs[mid], xs[i] = xs[i], xs[mid]
            mid += 1
    # Pivot will have been last element swapped down
    return mid-1


# Sorts xs[lwr:upr]
def quicksort_range(xs: list, lwr: int, upr: int) -> None:
    # Only need to do anything if not trivially sorted
    if upr - lwr > 1:
        # Partition and get index of pivot
        mid = partition(xs, lwr, upr)
        # Recursively sort everything before pivot (exclusive)
        quicksort_range(xs, lwr, mid)
        # Recursively sort everything after pivot (exclusive)
        quicksort_range(xs, mid+1, upr)


def quicksort(xs: list) -> list:
    quicksort_range(xs, 0, len(xs))
    return xs


def main():
    xs = [7, 1, 3, 0, 4, 6, 1, 4]
    print(xs)
    xs = quicksort(xs)
    print(xs)


if __name__ == '__main__':
    main()
