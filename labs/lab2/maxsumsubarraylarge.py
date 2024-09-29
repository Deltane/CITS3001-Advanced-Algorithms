def maxsumsubarraylarge(nums):
    max_sum = 0  # Initialize the maximum sum as 0
    current_sum = 0  # Initialize the current sum as 0

    for num in nums:
        current_sum = max(num, current_sum + num)  # Update current sum
        max_sum = max(max_sum, current_sum)  # Update max sum if current sum is larger

    return max_sum

def main():
    N = int(input())  # First line input, total number of elements
    nums = list(map(int, input().split()))  # Second line input, the array elements

    result = maxsumsubarraylarge(nums)
    print(result)

main()

"""Efficiency of Kadane’s Algorithm

Kadane’s algorithm runs in O(N) time complexity, where N is the number of elements in the array. This linear time complexity makes it suitable for even large inputs because it processes each element of the array exactly once. Here’s why:

	1.	Single Pass: Kadane’s algorithm only needs a single pass through the array, updating the current maximum subarray sum and the overall maximum subarray sum as it goes. It compares each element with the sum of that element and the current maximum subarray ending at the previous element. This decision determines whether to start a new subarray at the current element or continue with the existing subarray.
	2.	Constant Space: It uses a constant amount of extra space—only two variables to keep track of the current subarray sum and the maximum subarray sum found so far. This space efficiency is particularly important for large arrays to avoid memory overflow issues.

Handling Large Inputs

When the problem scales to an input size up to  N = 200,000  with array values ranging from  -10^9  to  10^9 :

	•	Efficiency Remains Intact: The linear time complexity of Kadane’s algorithm means it can handle up to 200,000 elements efficiently within a reasonable time frame for most competitive programming and real-world applications.
	•	Precision and Overflow: Python’s integer type can handle arbitrarily large integers, so even the sum of large integers won’t cause overflow, which might not be the case in languages with fixed integer sizes like C++ or Java."""