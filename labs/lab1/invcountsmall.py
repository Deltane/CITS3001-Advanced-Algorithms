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

def insertion_sort(xs: list): 
    # Iterate through prefix lengths 
    inversion_count = 0
    for l in range(1, len(xs)): 
        # Insert xs[l] into sorted prefix xs[0:l] 
        for i in range(l, 0, -1): 
            # xs[i] is element being inserted 
            if xs[i] < xs[i-1]: 
                # Wrong way around, swap them
                # Hint, this is an inversion!
                xs[i-1], xs[i] = xs[i], xs[i-1] 
                inversion_count +=1
            else: 
                # xs[i] is in the right spot 
                break 
        # xs[0:l+1] is now sorted 
    return inversion_count # Modify this to return the inversion count instead of the sorted list

def main():
    n = int(input())  # Read the number of elements
    xs = list(map(int, input().split()))  # Read the elements themselves
    if len(xs) != n:
        print("Error: The number of elements provided does not match the specified count.")
    else:
        print(insertion_sort(xs))

if __name__ == "__main__":
    main()

input = 1, 2, 3