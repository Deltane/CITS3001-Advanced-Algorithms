"""Inversion Count (large)
Problem ID: invcountlarge
Your task is to count the number of inversions in a list of integers. An inversion is a pair of indices (i, j) such that
i < j and A[i] > A[j].
Input
The first line of input contains an integer N (1 ≤ N ≤ 200 000), the number of integers in the list. Note that N
is provided for test case readability and your program does not need to use it. The second line contains N integers
A1, A2, . . . , AN (1 ≤ Ai ≤ 200 000).
Output
Display the number of inversions in the list.
"""


def merge_count_split_inv(arr, temp_arr, left, mid, right):
    i = left  # Starting index for left subarray
    j = mid + 1  # Starting index for right subarray
    k = left  # Starting index to be sorted
    inv_count = 0

    # Conditions are checked to ensure that i doesn't exceed mid and j doesn't exceed right
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            # There are mid - i inversions, because all the remaining elements in the left subarray
            # (arr[i], arr[i+1], ..., arr[mid]) are greater than arr[j]
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            j += 1
        k += 1

    # Copy the remaining elements of left subarray, if any
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    # Copy the remaining elements of right subarray, if any
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    # Copy the sorted subarray into Original array
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

    return inv_count

def merge_sort_and_count(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2

        inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
        inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)
        inv_count += merge_count_split_inv(arr, temp_arr, left, mid, right)

    return inv_count

def main():
    N = int(input())  # First line input, total number of elements
    arr = list(map(int, input().split()))  # Second line input, the array elements

    temp_arr = [0] * N
    result = merge_sort_and_count(arr, temp_arr, 0, N - 1)
    print(result)

main()

""" SOLUTION:
Algorithm:

Divide: Divide the array into two halves.
Conquer: Recursively sort each half.
Combine: Merge the sorted halves while counting inversions.

Explanation:

merge_and_count merges two sorted subarrays and counts inversions that occur between the two halves.
merge_sort_and_count recursively divides the array, sorts each half, and counts inversions during the merging process.
Time Complexity:

This modified approach has a time complexity of O(n log n), which is significantly more efficient for large inputs compared to the original O(n^2) implementation.
"""
