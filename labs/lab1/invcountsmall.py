"""Inversion Count (small)
Problem ID: invcountsmall
Your task is to count the number of inversions in a list of integers. An inversion is a pair of indices (i, j) such that
i < j and A[i] > A[j].
Input
The first line of input contains an integer N (1 ≤ N ≤ 10), the number of integers in the list. Note that N is provided
for test case readability and your program does not need to use it. The second line contains N integers A1, A2, . . . , AN
(1 ≤ Ai ≤ 10).
Output
Display the number of inversions in the list."""

def insertion_sort(items: list):
    # Count the number of inversions during the sorting process
    inversion_count = 0
    # Iterate through the items, starting with the second item
    for current_index in range(1, len(items)):
        # The current item is the one being inserted
        current_item = items[current_index]
        # Find the correct position for the current item in the sorted prefix
        for comparison_index in range(current_index, 0, -1):
            # Compare the current item with the previous item
            if current_item < items[comparison_index - 1]:
                # If they're in the wrong order, swap them
                items[comparison_index - 1], items[comparison_index] = items[comparison_index], items[comparison_index - 1]
                inversion_count += 1
            else:
                # If the current item is in the right place, break the loop
                break
    # The list is now sorted, so return the inversion count
    return inversion_count

def main():
    """Reads a list of integers from the user and performs insertion sort on it.

    Prints the number of inversions encountered.
    """

    num_elements = int(input())
    elements = list(map(int, input().split()))

    if len(elements) != num_elements:
        print("Error: The number of elements provided does not match the specified count.")
    else:
        print(insertion_sort(elements))

if __name__ == "__main__":
    main()

"""Understanding the Bottleneck:

Your current implementation, while correct, has a time complexity of O(n^2). This becomes inefficient for large input sizes. The primary bottleneck is the nested loop, where each element is compared with all preceding elements.

Solution: Merge Sort with Inversion Counting

A more efficient approach is to use Merge Sort, a divide-and-conquer algorithm that can be adapted to count inversions. The key idea is to count inversions while merging sorted subarrays."""